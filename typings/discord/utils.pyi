"""
This type stub file was generated by pyright.
"""

import array

"""
The MIT License (MIT)

Copyright (c) 2015-2020 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
DISCORD_EPOCH = ...
MAX_ASYNCIO_SECONDS = ...
class cached_property:
    def __init__(self, function) -> None:
        ...

    def __get__(self, instance, owner): # -> cached_property:
        ...



class CachedSlotProperty:
    def __init__(self, name, function) -> None:
        ...

    def __get__(self, instance, owner): # -> CachedSlotProperty | Any:
        ...



def cached_slot_property(name): # -> (func: Unknown) -> CachedSlotProperty:
    ...

class SequenceProxy(collections.abc.Sequence):
    """Read-only proxy of a Sequence."""
    def __init__(self, proxied) -> None:
        ...

    def __getitem__(self, idx):
        ...

    def __len__(self): # -> int:
        ...

    def __contains__(self, item): # -> bool:
        ...

    def __iter__(self): # -> Iterator[Unknown]:
        ...

    def __reversed__(self): # -> reversed[Unknown]:
        ...

    def index(self, value, *args, **kwargs):
        ...

    def count(self, value):
        ...



def parse_time(timestamp): # -> datetime | None:
    ...

def deprecated(instead=...): # -> (func: Unknown) -> (*args: Unknown, **kwargs: Unknown) -> Unknown:
    ...

def oauth_url(client_id, permissions=..., guild=..., redirect_uri=...): # -> str:
    """A helper function that returns the OAuth2 URL for inviting the bot
    into guilds.

    Parameters
    -----------
    client_id: :class:`str`
        The client ID for your bot.
    permissions: :class:`~discord.Permissions`
        The permissions you're requesting. If not given then you won't be requesting any
        permissions.
    guild: :class:`~discord.Guild`
        The guild to pre-select in the authorization screen, if available.
    redirect_uri: :class:`str`
        An optional valid redirect URI.

    Returns
    --------
    :class:`str`
        The OAuth2 URL for inviting the bot into guilds.
    """
    ...

def snowflake_time(id): # -> datetime:
    """
    Parameters
    -----------
    id: :class:`int`
        The snowflake ID.

    Returns
    --------
    :class:`datetime.datetime`
        The creation date in UTC of a Discord snowflake ID."""
    ...

def time_snowflake(datetime_obj, high=...): # -> Any | int:
    """Returns a numeric snowflake pretending to be created at the given date.

    When using as the lower end of a range, use ``time_snowflake(high=False) - 1`` to be inclusive, ``high=True`` to be exclusive
    When using as the higher end of a range, use ``time_snowflake(high=True)`` + 1 to be inclusive, ``high=False`` to be exclusive

    Parameters
    -----------
    datetime_obj: :class:`datetime.datetime`
        A timezone-naive datetime object representing UTC time.
    high: :class:`bool`
        Whether or not to set the lower 22 bit to high or low.
    """
    ...

def find(predicate, seq): # -> None:
    """A helper to return the first element found in the sequence
    that meets the predicate. For example: ::

        member = discord.utils.find(lambda m: m.name == 'Mighty', channel.guild.members)

    would find the first :class:`~discord.Member` whose name is 'Mighty' and return it.
    If an entry is not found, then ``None`` is returned.

    This is different from :func:`py:filter` due to the fact it stops the moment it finds
    a valid entry.

    Parameters
    -----------
    predicate
        A function that returns a boolean-like result.
    seq: iterable
        The iterable to search through.
    """
    ...

def get(iterable, **attrs): # -> None:
    r"""A helper that returns the first element in the iterable that meets
    all the traits passed in ``attrs``. This is an alternative for
    :func:`~discord.utils.find`.

    When multiple attributes are specified, they are checked using
    logical AND, not logical OR. Meaning they have to meet every
    attribute passed in and not one of them.

    To have a nested attribute search (i.e. search by ``x.y``) then
    pass in ``x__y`` as the keyword argument.

    If nothing is found that matches the attributes passed, then
    ``None`` is returned.

    Examples
    ---------

    Basic usage:

    .. code-block:: python3

        member = discord.utils.get(message.guild.members, name='Foo')

    Multiple attribute matching:

    .. code-block:: python3

        channel = discord.utils.get(guild.voice_channels, name='Foo', bitrate=64000)

    Nested attribute matching:

    .. code-block:: python3

        channel = discord.utils.get(client.get_all_channels(), guild__name='Cool', name='general')

    Parameters
    -----------
    iterable
        An iterable to search through.
    \*\*attrs
        Keyword arguments that denote attributes to search with.
    """
    ...

def to_json(obj): # -> str:
    ...

async def maybe_coroutine(f, *args, **kwargs): # -> Any:
    ...

async def async_all(gen, *, check=...): # -> bool:
    ...

async def sane_wait_for(futures, *, timeout): # -> Set[Unknown]:
    ...

async def sleep_until(when, result=...):
    """|coro|

    Sleep until a specified time.

    If the time supplied is in the past this function will yield instantly.

    .. versionadded:: 1.3

    Parameters
    -----------
    when: :class:`datetime.datetime`
        The timestamp in which to sleep until. If the datetime is naive then
        it is assumed to be in UTC.
    result: Any
        If provided is returned to the caller when the coroutine completes.
    """
    ...

def valid_icon_size(size): # -> bool:
    """Icons must be power of 2 within [16, 4096]."""
    ...

class SnowflakeList(array.array):
    """Internal data storage class to efficiently store a list of snowflakes.

    This should have the following characteristics:

    - Low memory usage
    - O(n) iteration (obviously)
    - O(n log n) initial creation if data is unsorted
    - O(log n) search and indexing
    - O(n) insertion
    """
    __slots__ = ...
    def __new__(cls, data, *, is_sorted=...):
        ...

    def add(self, element): # -> None:
        ...

    def get(self, element): # -> None:
        ...

    def has(self, element): # -> Literal[False]:
        ...



_IS_ASCII = ...
def resolve_invite(invite): # -> str | Any:
    """
    Resolves an invite from a :class:`~discord.Invite`, URL or code.

    Parameters
    -----------
    invite: Union[:class:`~discord.Invite`, :class:`str`]
        The invite.

    Returns
    --------
    :class:`str`
        The invite code.
    """
    ...

def resolve_template(code): # -> str | Any:
    """
    Resolves a template code from a :class:`~discord.Template`, URL or code.

    .. versionadded:: 1.4

    Parameters
    -----------
    code: Union[:class:`~discord.Template`, :class:`str`]
        The code.

    Returns
    --------
    :class:`str`
        The template code.
    """
    ...

_MARKDOWN_ESCAPE_SUBREGEX = ...
_MARKDOWN_ESCAPE_COMMON = ...
_MARKDOWN_ESCAPE_REGEX = ...
def escape_markdown(text, *, as_needed=..., ignore_links=...): # -> str:
    r"""A helper function that escapes Discord's markdown.

    Parameters
    -----------
    text: :class:`str`
        The text to escape markdown from.
    as_needed: :class:`bool`
        Whether to escape the markdown characters as needed. This
        means that it does not escape extraneous characters if it's
        not necessary, e.g. ``**hello**`` is escaped into ``\*\*hello**``
        instead of ``\*\*hello\*\*``. Note however that this can open
        you up to some clever syntax abuse. Defaults to ``False``.
    ignore_links: :class:`bool`
        Whether to leave links alone when escaping markdown. For example,
        if a URL in the text contains characters such as ``_`` then it will
        be left alone. This option is not supported with ``as_needed``.
        Defaults to ``True``.

    Returns
    --------
    :class:`str`
        The text with the markdown special characters escaped with a slash.
    """
    ...

def escape_mentions(text): # -> str:
    """A helper function that escapes everyone, here, role, and user mentions.

    .. note::

        This does not include channel mentions.

    .. note::

        For more granular control over what mentions should be escaped
        within messages, refer to the :class:`~discord.AllowedMentions`
        class.

    Parameters
    -----------
    text: :class:`str`
        The text to escape mentions from.

    Returns
    --------
    :class:`str`
        The text with the mentions removed.
    """
    ...
