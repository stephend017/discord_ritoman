"""
This type stub file was generated by pyright.
"""

from .mixins import Hashable

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
class TextChannel(discord.abc.Messageable, discord.abc.GuildChannel, Hashable):
    """Represents a Discord guild text channel.

    .. container:: operations

        .. describe:: x == y

            Checks if two channels are equal.

        .. describe:: x != y

            Checks if two channels are not equal.

        .. describe:: hash(x)

            Returns the channel's hash.

        .. describe:: str(x)

            Returns the channel's name.

    Attributes
    -----------
    name: :class:`str`
        The channel name.
    guild: :class:`Guild`
        The guild the channel belongs to.
    id: :class:`int`
        The channel ID.
    category_id: Optional[:class:`int`]
        The category channel ID this channel belongs to, if applicable.
    topic: Optional[:class:`str`]
        The channel's topic. ``None`` if it doesn't exist.
    position: :class:`int`
        The position in the channel list. This is a number that starts at 0. e.g. the
        top channel is position 0.
    last_message_id: Optional[:class:`int`]
        The last message ID of the message sent to this channel. It may
        *not* point to an existing or valid message.
    slowmode_delay: :class:`int`
        The number of seconds a member must wait between sending messages
        in this channel. A value of `0` denotes that it is disabled.
        Bots and users with :attr:`~Permissions.manage_channels` or
        :attr:`~Permissions.manage_messages` bypass slowmode.
    """
    __slots__ = ...
    def __init__(self, *, state, guild, data) -> None:
        ...

    def __repr__(self): # -> str:
        ...

    @property
    def type(self):
        """:class:`ChannelType`: The channel's Discord type."""
        ...

    def permissions_for(self, member): # -> Permissions:
        ...

    @property
    def members(self): # -> list[Unknown]:
        """List[:class:`Member`]: Returns all members that can see this channel."""
        ...

    def is_nsfw(self):
        """:class:`bool`: Checks if the channel is NSFW."""
        ...

    def is_news(self):
        """:class:`bool`: Checks if the channel is a news channel."""
        ...

    @property
    def last_message(self): # -> None:
        """Fetches the last message from this channel in cache.

        The message might not be valid or point to an existing message.

        .. admonition:: Reliable Fetching
            :class: helpful

            For a slightly more reliable method of fetching the
            last message, consider using either :meth:`history`
            or :meth:`fetch_message` with the :attr:`last_message_id`
            attribute.

        Returns
        ---------
        Optional[:class:`Message`]
            The last message in this channel or ``None`` if not found.
        """
        ...

    async def edit(self, *, reason=..., **options): # -> None:
        """|coro|

        Edits the channel.

        You must have the :attr:`~Permissions.manage_channels` permission to
        use this.

        .. versionchanged:: 1.3
            The ``overwrites`` keyword-only parameter was added.

        .. versionchanged:: 1.4
            The ``type`` keyword-only parameter was added.

        Parameters
        ----------
        name: :class:`str`
            The new channel name.
        topic: :class:`str`
            The new channel's topic.
        position: :class:`int`
            The new channel's position.
        nsfw: :class:`bool`
            To mark the channel as NSFW or not.
        sync_permissions: :class:`bool`
            Whether to sync permissions with the channel's new or pre-existing
            category. Defaults to ``False``.
        category: Optional[:class:`CategoryChannel`]
            The new category for this channel. Can be ``None`` to remove the
            category.
        slowmode_delay: :class:`int`
            Specifies the slowmode rate limit for user in this channel, in seconds.
            A value of `0` disables slowmode. The maximum value possible is `21600`.
        type: :class:`ChannelType`
            Change the type of this text channel. Currently, only conversion between
            :attr:`ChannelType.text` and :attr:`ChannelType.news` is supported. This
            is only available to guilds that contain ``NEWS`` in :attr:`Guild.features`.
        reason: Optional[:class:`str`]
            The reason for editing this channel. Shows up on the audit log.
        overwrites: :class:`dict`
            A :class:`dict` of target (either a role or a member) to
            :class:`PermissionOverwrite` to apply to the channel.

        Raises
        ------
        InvalidArgument
            If position is less than 0 or greater than the number of channels, or if
            the permission overwrite information is not in proper form.
        Forbidden
            You do not have permissions to edit the channel.
        HTTPException
            Editing the channel failed.
        """
        ...

    async def clone(self, *, name=..., reason=...): # -> TextChannel:
        ...

    async def delete_messages(self, messages): # -> None:
        """|coro|

        Deletes a list of messages. This is similar to :meth:`Message.delete`
        except it bulk deletes multiple messages.

        As a special case, if the number of messages is 0, then nothing
        is done. If the number of messages is 1 then single message
        delete is done. If it's more than two, then bulk delete is used.

        You cannot bulk delete more than 100 messages or messages that
        are older than 14 days old.

        You must have the :attr:`~Permissions.manage_messages` permission to
        use this.

        Usable only by bot accounts.

        Parameters
        -----------
        messages: Iterable[:class:`abc.Snowflake`]
            An iterable of messages denoting which ones to bulk delete.

        Raises
        ------
        ClientException
            The number of messages to delete was more than 100.
        Forbidden
            You do not have proper permissions to delete the messages or
            you're not using a bot account.
        NotFound
            If single delete, then the message was already deleted.
        HTTPException
            Deleting the messages failed.
        """
        ...

    async def purge(self, *, limit=..., check=..., before=..., after=..., around=..., oldest_first=..., bulk=...): # -> list[Unknown]:
        """|coro|

        Purges a list of messages that meet the criteria given by the predicate
        ``check``. If a ``check`` is not provided then all messages are deleted
        without discrimination.

        You must have the :attr:`~Permissions.manage_messages` permission to
        delete messages even if they are your own (unless you are a user
        account). The :attr:`~Permissions.read_message_history` permission is
        also needed to retrieve message history.

        Internally, this employs a different number of strategies depending
        on the conditions met such as if a bulk delete is possible or if
        the account is a user bot or not.

        Examples
        ---------

        Deleting bot's messages ::

            def is_me(m):
                return m.author == client.user

            deleted = await channel.purge(limit=100, check=is_me)
            await channel.send('Deleted {} message(s)'.format(len(deleted)))

        Parameters
        -----------
        limit: Optional[:class:`int`]
            The number of messages to search through. This is not the number
            of messages that will be deleted, though it can be.
        check: Callable[[:class:`Message`], :class:`bool`]
            The function used to check if a message should be deleted.
            It must take a :class:`Message` as its sole parameter.
        before: Optional[Union[:class:`abc.Snowflake`, :class:`datetime.datetime`]]
            Same as ``before`` in :meth:`history`.
        after: Optional[Union[:class:`abc.Snowflake`, :class:`datetime.datetime`]]
            Same as ``after`` in :meth:`history`.
        around: Optional[Union[:class:`abc.Snowflake`, :class:`datetime.datetime`]]
            Same as ``around`` in :meth:`history`.
        oldest_first: Optional[:class:`bool`]
            Same as ``oldest_first`` in :meth:`history`.
        bulk: :class:`bool`
            If ``True``, use bulk delete. Setting this to ``False`` is useful for mass-deleting
            a bot's own messages without :attr:`Permissions.manage_messages`. When ``True``, will
            fall back to single delete if current account is a user bot, or if messages are
            older than two weeks.

        Raises
        -------
        Forbidden
            You do not have proper permissions to do the actions required.
        HTTPException
            Purging the messages failed.

        Returns
        --------
        List[:class:`.Message`]
            The list of messages that were deleted.
        """
        ...

    async def webhooks(self): # -> list[Webhook]:
        """|coro|

        Gets the list of webhooks from this channel.

        Requires :attr:`~.Permissions.manage_webhooks` permissions.

        Raises
        -------
        Forbidden
            You don't have permissions to get the webhooks.

        Returns
        --------
        List[:class:`Webhook`]
            The webhooks for this channel.
        """
        ...

    async def create_webhook(self, *, name, avatar=..., reason=...): # -> Webhook:
        """|coro|

        Creates a webhook for this channel.

        Requires :attr:`~.Permissions.manage_webhooks` permissions.

        .. versionchanged:: 1.1
            Added the ``reason`` keyword-only parameter.

        Parameters
        -------------
        name: :class:`str`
            The webhook's name.
        avatar: Optional[:class:`bytes`]
            A :term:`py:bytes-like object` representing the webhook's default avatar.
            This operates similarly to :meth:`~ClientUser.edit`.
        reason: Optional[:class:`str`]
            The reason for creating this webhook. Shows up in the audit logs.

        Raises
        -------
        HTTPException
            Creating the webhook failed.
        Forbidden
            You do not have permissions to create a webhook.

        Returns
        --------
        :class:`Webhook`
            The created webhook.
        """
        ...

    async def follow(self, *, destination, reason=...): # -> Webhook:
        """
        Follows a channel using a webhook.

        Only news channels can be followed.

        .. note::

            The webhook returned will not provide a token to do webhook
            actions, as Discord does not provide it.

        .. versionadded:: 1.3

        Parameters
        -----------
        destination: :class:`TextChannel`
            The channel you would like to follow from.
        reason: Optional[:class:`str`]
            The reason for following the channel. Shows up on the destination guild's audit log.

            .. versionadded:: 1.4

        Raises
        -------
        HTTPException
            Following the channel failed.
        Forbidden
            You do not have the permissions to create a webhook.

        Returns
        --------
        :class:`Webhook`
            The created webhook.
        """
        ...

    def get_partial_message(self, message_id): # -> PartialMessage:
        """Creates a :class:`PartialMessage` from the message ID.

        This is useful if you want to work with a message and only have its ID without
        doing an unnecessary API call.

        .. versionadded:: 1.6

        Parameters
        ------------
        message_id: :class:`int`
            The message ID to create a partial message for.

        Returns
        ---------
        :class:`PartialMessage`
            The partial message.
        """
        ...



class VoiceChannel(discord.abc.Connectable, discord.abc.GuildChannel, Hashable):
    """Represents a Discord guild voice channel.

    .. container:: operations

        .. describe:: x == y

            Checks if two channels are equal.

        .. describe:: x != y

            Checks if two channels are not equal.

        .. describe:: hash(x)

            Returns the channel's hash.

        .. describe:: str(x)

            Returns the channel's name.

    Attributes
    -----------
    name: :class:`str`
        The channel name.
    guild: :class:`Guild`
        The guild the channel belongs to.
    id: :class:`int`
        The channel ID.
    category_id: Optional[:class:`int`]
        The category channel ID this channel belongs to, if applicable.
    position: :class:`int`
        The position in the channel list. This is a number that starts at 0. e.g. the
        top channel is position 0.
    bitrate: :class:`int`
        The channel's preferred audio bitrate in bits per second.
    user_limit: :class:`int`
        The channel's limit for number of members that can be in a voice channel.
    """
    __slots__ = ...
    def __init__(self, *, state, guild, data) -> None:
        ...

    def __repr__(self): # -> str:
        ...

    @property
    def type(self): # -> int:
        """:class:`ChannelType`: The channel's Discord type."""
        ...

    @property
    def members(self): # -> list[Unknown]:
        """List[:class:`Member`]: Returns all members that are currently inside this voice channel."""
        ...

    @property
    def voice_states(self): # -> dict[Unknown, Unknown]:
        """Returns a mapping of member IDs who have voice states in this channel.

        .. versionadded:: 1.3

        .. note::

            This function is intentionally low level to replace :attr:`members`
            when the member cache is unavailable.

        Returns
        --------
        Mapping[:class:`int`, :class:`VoiceState`]
            The mapping of member ID to a voice state.
        """
        ...

    def permissions_for(self, member): # -> Permissions:
        ...

    async def clone(self, *, name=..., reason=...): # -> VoiceChannel:
        ...

    async def edit(self, *, reason=..., **options): # -> None:
        """|coro|

        Edits the channel.

        You must have the :attr:`~Permissions.manage_channels` permission to
        use this.

        .. versionchanged:: 1.3
            The ``overwrites`` keyword-only parameter was added.

        Parameters
        ----------
        name: :class:`str`
            The new channel's name.
        bitrate: :class:`int`
            The new channel's bitrate.
        user_limit: :class:`int`
            The new channel's user limit.
        position: :class:`int`
            The new channel's position.
        sync_permissions: :class:`bool`
            Whether to sync permissions with the channel's new or pre-existing
            category. Defaults to ``False``.
        category: Optional[:class:`CategoryChannel`]
            The new category for this channel. Can be ``None`` to remove the
            category.
        reason: Optional[:class:`str`]
            The reason for editing this channel. Shows up on the audit log.
        overwrites: :class:`dict`
            A :class:`dict` of target (either a role or a member) to
            :class:`PermissionOverwrite` to apply to the channel.

        Raises
        ------
        InvalidArgument
            If the permission overwrite information is not in proper form.
        Forbidden
            You do not have permissions to edit the channel.
        HTTPException
            Editing the channel failed.
        """
        ...



class CategoryChannel(discord.abc.GuildChannel, Hashable):
    """Represents a Discord channel category.

    These are useful to group channels to logical compartments.

    .. container:: operations

        .. describe:: x == y

            Checks if two channels are equal.

        .. describe:: x != y

            Checks if two channels are not equal.

        .. describe:: hash(x)

            Returns the category's hash.

        .. describe:: str(x)

            Returns the category's name.

    Attributes
    -----------
    name: :class:`str`
        The category name.
    guild: :class:`Guild`
        The guild the category belongs to.
    id: :class:`int`
        The category channel ID.
    position: :class:`int`
        The position in the category list. This is a number that starts at 0. e.g. the
        top category is position 0.
    """
    __slots__ = ...
    def __init__(self, *, state, guild, data) -> None:
        ...

    def __repr__(self): # -> str:
        ...

    @property
    def type(self): # -> int:
        """:class:`ChannelType`: The channel's Discord type."""
        ...

    def is_nsfw(self):
        """:class:`bool`: Checks if the category is NSFW."""
        ...

    async def clone(self, *, name=..., reason=...): # -> CategoryChannel:
        ...

    async def edit(self, *, reason=..., **options): # -> None:
        """|coro|

        Edits the channel.

        You must have the :attr:`~Permissions.manage_channels` permission to
        use this.

        .. versionchanged:: 1.3
            The ``overwrites`` keyword-only parameter was added.

        Parameters
        ----------
        name: :class:`str`
            The new category's name.
        position: :class:`int`
            The new category's position.
        nsfw: :class:`bool`
            To mark the category as NSFW or not.
        reason: Optional[:class:`str`]
            The reason for editing this category. Shows up on the audit log.
        overwrites: :class:`dict`
            A :class:`dict` of target (either a role or a member) to
            :class:`PermissionOverwrite` to apply to the channel.

        Raises
        ------
        InvalidArgument
            If position is less than 0 or greater than the number of categories.
        Forbidden
            You do not have permissions to edit the category.
        HTTPException
            Editing the category failed.
        """
        ...

    @property
    def channels(self): # -> list[Unknown]:
        """List[:class:`abc.GuildChannel`]: Returns the channels that are under this category.

        These are sorted by the official Discord UI, which places voice channels below the text channels.
        """
        ...

    @property
    def text_channels(self): # -> list[TextChannel]:
        """List[:class:`TextChannel`]: Returns the text channels that are under this category."""
        ...

    @property
    def voice_channels(self): # -> list[VoiceChannel]:
        """List[:class:`VoiceChannel`]: Returns the voice channels that are under this category."""
        ...

    async def create_text_channel(self, name, *, overwrites=..., reason=..., **options):
        """|coro|

        A shortcut method to :meth:`Guild.create_text_channel` to create a :class:`TextChannel` in the category.

        Returns
        -------
        :class:`TextChannel`
            The channel that was just created.
        """
        ...

    async def create_voice_channel(self, name, *, overwrites=..., reason=..., **options):
        """|coro|

        A shortcut method to :meth:`Guild.create_voice_channel` to create a :class:`VoiceChannel` in the category.

        Returns
        -------
        :class:`VoiceChannel`
            The channel that was just created.
        """
        ...



class StoreChannel(discord.abc.GuildChannel, Hashable):
    """Represents a Discord guild store channel.

    .. container:: operations

        .. describe:: x == y

            Checks if two channels are equal.

        .. describe:: x != y

            Checks if two channels are not equal.

        .. describe:: hash(x)

            Returns the channel's hash.

        .. describe:: str(x)

            Returns the channel's name.

    Attributes
    -----------
    name: :class:`str`
        The channel name.
    guild: :class:`Guild`
        The guild the channel belongs to.
    id: :class:`int`
        The channel ID.
    category_id: :class:`int`
        The category channel ID this channel belongs to.
    position: :class:`int`
        The position in the channel list. This is a number that starts at 0. e.g. the
        top channel is position 0.
    """
    __slots__ = ...
    def __init__(self, *, state, guild, data) -> None:
        ...

    def __repr__(self): # -> str:
        ...

    @property
    def type(self): # -> int:
        """:class:`ChannelType`: The channel's Discord type."""
        ...

    def permissions_for(self, member): # -> Permissions:
        ...

    def is_nsfw(self):
        """:class:`bool`: Checks if the channel is NSFW."""
        ...

    async def clone(self, *, name=..., reason=...): # -> StoreChannel:
        ...

    async def edit(self, *, reason=..., **options): # -> None:
        """|coro|

        Edits the channel.

        You must have the :attr:`~Permissions.manage_channels` permission to
        use this.

        Parameters
        ----------
        name: :class:`str`
            The new channel name.
        position: :class:`int`
            The new channel's position.
        nsfw: :class:`bool`
            To mark the channel as NSFW or not.
        sync_permissions: :class:`bool`
            Whether to sync permissions with the channel's new or pre-existing
            category. Defaults to ``False``.
        category: Optional[:class:`CategoryChannel`]
            The new category for this channel. Can be ``None`` to remove the
            category.
        reason: Optional[:class:`str`]
            The reason for editing this channel. Shows up on the audit log.
        overwrites: :class:`dict`
            A :class:`dict` of target (either a role or a member) to
            :class:`PermissionOverwrite` to apply to the channel.

            .. versionadded:: 1.3

        Raises
        ------
        InvalidArgument
            If position is less than 0 or greater than the number of channels, or if
            the permission overwrite information is not in proper form.
        Forbidden
            You do not have permissions to edit the channel.
        HTTPException
            Editing the channel failed.
        """
        ...



class DMChannel(discord.abc.Messageable, Hashable):
    """Represents a Discord direct message channel.

    .. container:: operations

        .. describe:: x == y

            Checks if two channels are equal.

        .. describe:: x != y

            Checks if two channels are not equal.

        .. describe:: hash(x)

            Returns the channel's hash.

        .. describe:: str(x)

            Returns a string representation of the channel

    Attributes
    ----------
    recipient: :class:`User`
        The user you are participating with in the direct message channel.
    me: :class:`ClientUser`
        The user presenting yourself.
    id: :class:`int`
        The direct message channel ID.
    """
    __slots__ = ...
    def __init__(self, *, me, state, data) -> None:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self): # -> str:
        ...

    @property
    def type(self): # -> int:
        """:class:`ChannelType`: The channel's Discord type."""
        ...

    @property
    def created_at(self): # -> datetime:
        """:class:`datetime.datetime`: Returns the direct message channel's creation time in UTC."""
        ...

    def permissions_for(self, user=...): # -> Permissions:
        """Handles permission resolution for a :class:`User`.

        This function is there for compatibility with other channel types.

        Actual direct messages do not really have the concept of permissions.

        This returns all the Text related permissions set to ``True`` except:

        - :attr:`~Permissions.send_tts_messages`: You cannot send TTS messages in a DM.
        - :attr:`~Permissions.manage_messages`: You cannot delete others messages in a DM.

        Parameters
        -----------
        user: :class:`User`
            The user to check permissions for. This parameter is ignored
            but kept for compatibility.

        Returns
        --------
        :class:`Permissions`
            The resolved permissions.
        """
        ...

    def get_partial_message(self, message_id): # -> PartialMessage:
        """Creates a :class:`PartialMessage` from the message ID.

        This is useful if you want to work with a message and only have its ID without
        doing an unnecessary API call.

        .. versionadded:: 1.6

        Parameters
        ------------
        message_id: :class:`int`
            The message ID to create a partial message for.

        Returns
        ---------
        :class:`PartialMessage`
            The partial message.
        """
        ...



class GroupChannel(discord.abc.Messageable, Hashable):
    """Represents a Discord group channel.

    .. container:: operations

        .. describe:: x == y

            Checks if two channels are equal.

        .. describe:: x != y

            Checks if two channels are not equal.

        .. describe:: hash(x)

            Returns the channel's hash.

        .. describe:: str(x)

            Returns a string representation of the channel

    Attributes
    ----------
    recipients: List[:class:`User`]
        The users you are participating with in the group channel.
    me: :class:`ClientUser`
        The user presenting yourself.
    id: :class:`int`
        The group channel ID.
    owner: :class:`User`
        The user that owns the group channel.
    icon: Optional[:class:`str`]
        The group channel's icon hash if provided.
    name: Optional[:class:`str`]
        The group channel's name if provided.
    """
    __slots__ = ...
    def __init__(self, *, me, state, data) -> None:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self): # -> str:
        ...

    @property
    def type(self): # -> int:
        """:class:`ChannelType`: The channel's Discord type."""
        ...

    @property
    def icon_url(self): # -> Asset:
        """:class:`Asset`: Returns the channel's icon asset if available.

        This is equivalent to calling :meth:`icon_url_as` with
        the default parameters ('webp' format and a size of 1024).
        """
        ...

    def icon_url_as(self, *, format=..., size=...): # -> Asset:
        """Returns an :class:`Asset` for the icon the channel has.

        The format must be one of 'webp', 'jpeg', 'jpg' or 'png'.
        The size must be a power of 2 between 16 and 4096.

        .. versionadded:: 2.0

        Parameters
        -----------
        format: :class:`str`
            The format to attempt to convert the icon to. Defaults to 'webp'.
        size: :class:`int`
            The size of the image to display.

        Raises
        ------
        InvalidArgument
            Bad image format passed to ``format`` or invalid ``size``.

        Returns
        --------
        :class:`Asset`
            The resulting CDN asset.
        """
        ...

    @property
    def created_at(self): # -> datetime:
        """:class:`datetime.datetime`: Returns the channel's creation time in UTC."""
        ...

    def permissions_for(self, user): # -> Permissions:
        """Handles permission resolution for a :class:`User`.

        This function is there for compatibility with other channel types.

        Actual direct messages do not really have the concept of permissions.

        This returns all the Text related permissions set to ``True`` except:

        - send_tts_messages: You cannot send TTS messages in a DM.
        - manage_messages: You cannot delete others messages in a DM.

        This also checks the kick_members permission if the user is the owner.

        Parameters
        -----------
        user: :class:`User`
            The user to check permissions for.

        Returns
        --------
        :class:`Permissions`
            The resolved permissions for the user.
        """
        ...

    async def add_recipients(self, *recipients): # -> None:
        r"""|coro|

        Adds recipients to this group.

        A group can only have a maximum of 10 members.
        Attempting to add more ends up in an exception. To
        add a recipient to the group, you must have a relationship
        with the user of type :attr:`RelationshipType.friend`.

        Parameters
        -----------
        \*recipients: :class:`User`
            An argument list of users to add to this group.

        Raises
        -------
        HTTPException
            Adding a recipient to this group failed.
        """
        ...

    async def remove_recipients(self, *recipients): # -> None:
        r"""|coro|

        Removes recipients from this group.

        Parameters
        -----------
        \*recipients: :class:`User`
            An argument list of users to remove from this group.

        Raises
        -------
        HTTPException
            Removing a recipient from this group failed.
        """
        ...

    async def edit(self, **fields): # -> None:
        """|coro|

        Edits the group.

        Parameters
        -----------
        name: Optional[:class:`str`]
            The new name to change the group to.
            Could be ``None`` to remove the name.
        icon: Optional[:class:`bytes`]
            A :term:`py:bytes-like object` representing the new icon.
            Could be ``None`` to remove the icon.

        Raises
        -------
        HTTPException
            Editing the group failed.
        """
        ...

    async def leave(self): # -> None:
        """|coro|

        Leave the group.

        If you are the only one in the group, this deletes it as well.

        Raises
        -------
        HTTPException
            Leaving the group failed.
        """
        ...
