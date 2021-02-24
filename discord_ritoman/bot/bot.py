from discord_ritoman.db.schema import LoLUser
from discord_ritoman.db.accessors import (
    get_lol_user_by_discord_id,
    set_lol_user_winrate,
)
from discord.ext import commands

from discord_ritoman.utils import create_logger


bot = commands.Bot(command_prefix="<@!779328785043554334> ")

logger = create_logger(__file__)


# TODO flame command
# scenario cj talking shit, akshay wants to put him
# in his place. the solution the flame command.
# askhay invokes @ritoman flame @Mars. the bot then
# searches for a statline that is better for akshay
# command will not work if akshay does not play LoL


async def winrate_add_helper(ctx, user: LoLUser):
    """
    winrate add helper function (to reduce single function complexity)

    Args:
        ctx: the discord context object sent to the command function
        username: the username of the discord user
    """
    if user.winrate:
        await ctx.send("<:PepoG:773739956958658560>")
        return

    username: str = ""
    try:
        username = (await bot.fetch_user(user.discord_id)).name
    except Exception:
        await ctx.send("<:PepoG:773739956958658560>")
        return

    set_lol_user_winrate(user, True)
    await ctx.send(f"successfully added {username}")


async def winrate_remove_helper(ctx, user: LoLUser):
    """
    winrate helper function (to reduce single function complexity)

    Args:
        ctx: the discord context object sent to the command function
        username: the username of the discord user
    """
    if not user.winrate:
        await ctx.send("<:PepoG:773739956958658560>")
        return

    username: str = ""
    try:
        username = (await bot.fetch_user(user.discord_id)).name
    except Exception:
        await ctx.send("<:PepoG:773739956958658560>")
        return

    set_lol_user_winrate(user, False)

    await ctx.send(f"successfully removed {username}")


async def winrate_get_helper(ctx, user: LoLUser):
    """
    winrate helper function (to reduce single function complexity)

    Args:
        ctx: the discord context object sent to the command function
        username: the username of the discord user
        user_id: the discord id of the discord user
    """
    if not user.winrate:
        await ctx.send("<:PepoG:773739956958658560>")
        return

    await ctx.send(
        f"the winrate for <@!{user.discord_id}> today is {user.wins} wins and {user.losses} losses"
    )


@bot.command()
async def winrate(ctx, option, discord_user):
    """
    The winrate command for the discord ritoman bot

    Args:
        option: What specific subcommand to run (--add, --remove, --get)
        discord_user: should be a server member in the form of @username
    """
    user_id = int(discord_user[3:-1])
    user = get_lol_user_by_discord_id(user_id)

    if user is None:
        await ctx.send("<:PepoG:773739956958658560>")
        return

    if option == "--add":
        return await winrate_add_helper(ctx, user)
    elif option == "--remove":
        return await winrate_remove_helper(ctx, user)
    elif option == "--get":
        return await winrate_get_helper(ctx, user)

    await ctx.send("<:PepoG:773739956958658560>")
