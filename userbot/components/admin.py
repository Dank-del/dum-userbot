# there cus why not ? :P
from pyrogram.methods import messages
from pyrogram.types import Message
from pyrogram import Client, filters
from userbot import botclient as cl, bot_prefixes
from userbot.helpers.messages import get_id_or_username
from userbot.helpers.html_enc import bold, code

@cl.on_message(filters.me & filters.command("ban", prefixes=bot_prefixes))
def ban_user(client: Client, message: Message):
    user_id_or_username = get_id_or_username(message)
    user = client.get_chat(user_id_or_username)
    try:
        client.kick_chat_member(user_id=user.id, chat_id=message.chat.id)
        message.reply("{} {}".format(user.mention, bold("was banned")))
        return
    except BaseException as ex:
        message.reply("{}: {}".format(bold("Failed due to"), code(str(ex))))
        return


@cl.on_message(filters.me & filters.command("unban", prefixes=bot_prefixes))
def unban_user(client: Client, message: Message):
    user_id_or_username = get_id_or_username(message)
    user = client.get_chat(user_id_or_username)
    try:
        client.unban_chat_member(user_id=user.id, chat_id=message.chat.id)
        message.reply("{} {}".format(user.mention, bold("was unbanned")))
        return
    except BaseException as ex:
        message.reply("{}: {}".format(bold("Failed due to"), code(str(ex))))
        return


@cl.on_message(filters.me & filters.command("kick", prefixes=bot_prefixes))
def kick_user(client: Client, message: Message):
    user_id_or_username = get_id_or_username(message)
    user = client.get_chat(user_id_or_username)
    try:
        client.kick_chat_member(user_id=user.id, chat_id=message.chat.id)
        client.unban_chat_member(user_id=user.id, chat_id=message.chat.id)
        message.reply("{} {}".format(user.mention, bold("was banned")))
        return
    except BaseException as ex:
        message.reply("{}: {}".format(bold("Failed due to"), code(str(ex))))
        return