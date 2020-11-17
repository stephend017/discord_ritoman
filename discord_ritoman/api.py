from sys import prefix
from discord_ritoman.discord_api import send_discord_message
from typing import Any, Dict, List
from discord_ritoman.lol_match_metadata import LoLMatchMetadata
from discord_ritoman.db_api import (
    get_all_discord_users,
    get_all_prefixes,
    get_last_recorded_time,
    set_last_recorded_time,
    get_all_stat_prefixes_01,
    get_all_suffixes,
)
from discord_ritoman.lol_api import (
    get_account_id,
    get_matches,
    get_match_data,
    get_match_timeline,
)
from discord_ritoman.lol_match_data import LoLMatchData
import random


def run_lol():
    """
    This is the function that updates and sends messages
    to the discord server for every bad game
    """
    users = get_all_discord_users()
    prefixes = get_all_prefixes()
    stat_prefixes_01 = get_all_stat_prefixes_01()
    suffixes = get_all_suffixes()

    for user_info in users:
        timestamp = get_last_recorded_time(user_info[0])

        account_id: str = ""
        matches: List[LoLMatchMetadata] = []

        try:
            account_id = get_account_id(user_info[1])
            matches = get_matches(account_id, timestamp)
        except Exception:
            print(
                "There was an error retrieving account data, skipping this iteration"
            )
            continue

        for match in matches:
            match_data: Dict[str, Any] = {}
            match_timeline: Dict[str, Any] = {}

            try:
                match_data = get_match_data(match.game_id)
                match_timeline = get_match_timeline(match.game_id)
            except Exception:
                print(
                    "There was an error retrieving match data, skipping this iteration"
                )
                continue

            data = LoLMatchData(match_data, match_timeline)

            # check if the user lost and had less solo kills
            # than solo deaths
            if not data.did_account_win(account_id):
                solo_kills: int = data.get_solo_kills(account_id)
                solo_deaths: int = data.get_solo_killed(account_id)
                if solo_kills < solo_deaths:
                    prefix_index: int = random.randint(0, len(prefixes) - 1)
                    stat_prefix_01_index: int = random.randint(
                        0, len(stat_prefixes_01) - 1
                    )
                    suffix_index: int = random.randint(0, len(suffixes) - 1)
                    send_discord_message(
                        f"{prefixes[prefix_index][0]} <@{user_info[2]}> {stat_prefixes_01[stat_prefix_01_index][0]} {solo_deaths} solo deaths and only {solo_kills} solo kills in their latest defeat in league of legends. {suffixes[suffix_index][0]}"
                    )

            set_last_recorded_time(user_info[0], data.get_match_end())
