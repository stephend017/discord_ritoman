"""
This type stub file was generated by pyright.
"""

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
class _EmojiTag:
    __slots__ = ...


class PartialEmoji(_EmojiTag):
    """Represents a "partial" emoji.

    This model will be given in two scenarios:

    - "Raw" data events such as :func:`on_raw_reaction_add`
    - Custom emoji that the bot cannot see from e.g. :attr:`Message.reactions`

    .. container:: operations

        .. describe:: x == y

            Checks if two emoji are the same.

        .. describe:: x != y

            Checks if two emoji are not the same.

        .. describe:: hash(x)

            Return the emoji's hash.

        .. describe:: str(x)

            Returns the emoji rendered for discord.

    Attributes
    -----------
    name: Optional[:class:`str`]
        The custom emoji name, if applicable, or the unicode codepoint
        of the non-custom emoji. This can be ``None`` if the emoji
        got deleted (e.g. removing a reaction with a deleted emoji).
    animated: :class:`bool`
        Whether the emoji is animated or not.
    id: Optional[:class:`int`]
        The ID of the custom emoji, if applicable.
    """
    __slots__ = ...
    def __init__(self, *, name, animated=..., id=...) -> None:
        ...

    @classmethod
    def from_dict(cls, data): # -> PartialEmoji:
        ...

    def to_dict(self): # -> dict[str, Unknown]:
        ...

    @classmethod
    def with_state(cls, state, *, name, animated=..., id=...): # -> PartialEmoji:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self): # -> str:
        ...

    def __eq__(self, other) -> bool:
        ...

    def __ne__(self, other) -> bool:
        ...

    def __hash__(self) -> int:
        ...

    def is_custom_emoji(self): # -> bool:
        """:class:`bool`: Checks if this is a custom non-Unicode emoji."""
        ...

    def is_unicode_emoji(self): # -> bool:
        """:class:`bool`: Checks if this is a Unicode emoji."""
        ...

    @property
    def created_at(self): # -> datetime | None:
        """Optional[:class:`datetime.datetime`]: Returns the emoji's creation time in UTC, or None if Unicode emoji.

        .. versionadded:: 1.6
        """
        ...

    @property
    def url(self): # -> Asset:
        """:class:`Asset`: Returns an asset of the emoji, if it is custom."""
        ...
