from userbot.helpers.messages import get_id_or_username
from userbot.helpers.html_enc import bold, code, mention
from pyrogram import filters, Client
from userbot import botclient as cl, bot_prefixes
from pyrogram.types import Message

@cl.on_message(filters.me & filters.command("uinfo", prefixes=bot_prefixes))
def uinfo(client: Client, message: Message):
    """Get user information"""
    user = client.get_chat(get_id_or_username(message))
    if not user:
        return
    if user.username:
        client.send_message(message.chat.id, f"{bold('Username')}: @{user.username}\n"
                                          f"{bold('First name')}: {user.first_name}\n"
                                          f"{bold('Last name')}: {user.last_name}\n"
                                          f"ID: {code(str(user.id))}\n"
                                          f"{bold('Link')}: {mention(text='here', id=user.id)}", parse_mode='html')
    else:
        client.send_message(message.chat.id, f"{bold('First name')}: {user.first_name}\n"
                                          f"{bold('Last name')}: {user.last_name}\n"
                                          f"ID: {code(str(user.id))}\n"
                                          f"{bold('Link')}: {mention(text='here', id=user.id)}", parse_mode='html')