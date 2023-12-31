from datetime import datetime

import discord
import peewee

from database.models.base import DefaultDatabaseModel
from database.models.command import Command, DiscordUser


class Message(DefaultDatabaseModel):
    discord_id: peewee.BigIntegerField = peewee.BigIntegerField(unique=True)
    content: peewee.TextField = peewee.TextField(null=False)
    created_at: peewee.DateTimeField = peewee.DateTimeField(default=datetime.now())
    edited_at: peewee.DateTimeField = peewee.DateTimeField(null=True, default=None)
    user: peewee.ForeignKeyField = peewee.ForeignKeyField(
        DiscordUser, backref="messages", on_delete="CASCADE"
    )
    command: peewee.ForeignKeyField = peewee.ForeignKeyField(
        Command, backref="messages", on_delete="SET NULL", null=True
    )
    reaction_counter: peewee.IntegerField = peewee.IntegerField(default=0)

    @classmethod
    def create_new_message(
        cls,
        sent_message: discord.Message,
        user: peewee.ForeignKeyField,
        command: peewee.ForeignKeyField = None,
    ):
        return cls.create(
            discord_id=sent_message.id,
            content=sent_message.content,
            created_at=sent_message.created_at,
            user=user,
            command=command,
        )

    @classmethod
    def edit_message(
        cls,
        discord_id: peewee.BigIntegerField,
        edited_message: discord.Message = None,
        reaction_counter: peewee.IntegerField = None,
    ):
        if reaction_counter:
            return (
                cls.update(reaction_counter=reaction_counter)
                .where(cls.discord_id == discord_id)
                .execute()
            )

        return (
            cls.update(
                content=edited_message.content, edited_at=edited_message.edited_at
            )
            .where(cls.discord_id == discord_id)
            .execute()
        )

    def __str__(self) -> str:
        return f"Message {self.id}"
