"""
Interface for accessing riot API
"""
from datetime import timedelta
from sd_utils.api.rate_limit import RateLimit
from discord_ritoman.utils import create_logger
from discord_ritoman.lru_cache import lru_cache
from typing import Any, List, Optional
from discord_ritoman.lol_match_metadata import (
    LoLMatchMetadata,
    LoLMatchStartData,
)
import requests
import os
import sys
from sd_utils.api.client import Client
from sd_utils.api.request import Request
from sd_utils.api.error import Error

logger = create_logger(__file__)

RIOT_TOKEN = os.getenv("RIOT_TOKEN", None)


class RiotAPIResponseHandler:
    """
    class to define custom response behavior from the riot_api_get function
    """

    def __init__(self, status_code: int, handler: Any):
        self.status_code = status_code
        self.handler = handler


def riot_api_get(
    url: str, custom_handlers: List[RiotAPIResponseHandler] = []
) -> Any:
    """
    Generic method for making a GET request to the riot API

    Args:
        url (str): the url endpoint of the request
        custom_handlers (List[RiotAPIResponseHandler]): custom handlers for non 200
            status codes

    Returns:
        Any: the json object returned by a successful request
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": RIOT_TOKEN,
    }
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json()

    # process custom handlers first
    for ch in custom_handlers:
        if ch.status_code == response.status_code:
            return ch.handler(response)

    if response.status_code == 403:
        logger.critical("Invalid API token. Stopping program")
        sys.exit(0)

    if response.status_code == 429:
        logger.warn(
            f"Rate limit exceeded when making request [{response.text}]"
        )
        # TODO queue request
        return

    logger.critical(
        f"GET riot request failed: URL: [{url}] [{response.status_code}] {response.text}"
    )
    raise Exception(
        f"GET riot request failed: URL: [{url}] [{response.status_code}] {response.text}"
    )


@lru_cache
def get_account_id(puuid: str) -> str:
    """
    Returns the accountId for a given riot puuid

    Note: the PUUID must be from the summoner API. The
    current API token does not support the account API

    Args:
        puuid (str): the riot puuid (see riot developer docs)

    Returns:
        accoundId (str): the riot accountId associated with the
            given PUUID
    """
    url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
    return riot_api_get(url)["accountId"]


def get_matches(
    account_id: str, start_timestamp: int
) -> List[LoLMatchMetadata]:
    """
    Returns all the matches for a given account Id after the specified timestamp

    If no matches are found (404) then this function returns an empty list

    Args:
        account_id (str): the riot puuid of the account
        start_timestamp (int): the timestamp in ms since the epoch
            from when to start looking for matches

    Returns:
        List[LoLMatchMetadata]: all the matches found from the user after the
            given timestamp
    """
    url = f"https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{account_id}?beginTime={start_timestamp}"
    response = riot_api_get(
        url,
        custom_handlers=[
            RiotAPIResponseHandler(404, lambda response: {"matches": []})
        ],
    )

    return [
        LoLMatchMetadata(item["gameId"], item["champion"], item["timestamp"])
        for item in response["matches"]
    ]


@lru_cache
def get_match_data(match_id: int) -> Any:
    """
    Returns all the match data for a given match

    This returns information about the match, mainly
    overall statistics, team compositions and state of
    the match when it ended

    Args:
        match_id (int): the numeric identifier for a
            match (see riot developer docs)

    Returns:
        Any: the full json response from the riot API
    """
    url = f"https://na1.api.riotgames.com/lol/match/v4/matches/{match_id}"
    return riot_api_get(url)


@lru_cache
def get_match_timeline(match_id: int) -> Any:
    """
    Returns a timeline of the match

    Args:
        match_id (int): the numeric identifier for the match

    Returns:
        Any: the full json response from the riot API
    """
    url = f"https://na1.api.riotgames.com/lol/match/v4/timelines/by-match/{match_id}"
    return riot_api_get(url)


def get_puuid(summoner_name: str) -> str:
    """
    Returns a riot puuid based on a summoner name

    Args:
        summoner_name (str): the name of the summoner
            to get a puuid for

    Returns:
        str: the puuid for the given summoner
    """

    url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    return riot_api_get(url)["puuid"]


def get_encrypted_summoner_id(puuid: str) -> str:
    """
    Returns a riot encrypted summoner id based on a summoner puuid

    Args:
        summoner_name (str): the puuid of the summoner
            to get a encrypted summoner id for

    Returns:
        str: the encrypted summoner id for the given summoner
    """

    url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
    return riot_api_get(url)["id"]


def get_active_game(encrypted_summoner_id: str) -> Optional[LoLMatchStartData]:
    """
    TODO
    """
    url = f"https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{encrypted_summoner_id}"
    response = riot_api_get(
        url,
        custom_handlers=[RiotAPIResponseHandler(404, lambda response: None)],
    )

    if response is None:
        return None

    return LoLMatchStartData(
        response["gameId"],
        response["gameMode"],
        int(response["gameStartTime"]),
    )


class RiotAPI(
    metaclass=Client(
        "https://na1.api.riotgames.com/lol",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://developer.riotgames.com",
            "X-Riot-Token": RIOT_TOKEN,
        },
    )
):
    get_active_game: Request = Request(
        "GET",
        "/spectator/v4/active-games/by-summoner",
        rate_limits=[
            RateLimit(20, timedelta(seconds=1)),
            RateLimit(100, timedelta(minutes=2)),
        ],
    )

    get_encrypted_summoner_id: Request = Request(
        "GET",
        "/summoner/v4/summoners/by-puuid",
        rate_limits=[
            RateLimit(20, timedelta(seconds=1)),
            RateLimit(100, timedelta(minutes=2)),
        ],
    )
    """
    Returns a riot encrypted summoner id based on a summoner puuid

    Args:
        summoner_name (str): the puuid of the summoner
            to get a encrypted summoner id for

    Returns:
        str: the encrypted summoner id for the given summoner
    """
    rate_limit_exceeded = Error(429, "Rate Limit Exceeded",)
