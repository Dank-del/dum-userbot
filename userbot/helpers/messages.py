from pyrogram.types import Message

def get_id_or_username(message: Message) -> int:
    '''
    Get user ID or username from message
    '''
    if len(message.command) > 1:
        return message.command[1]
    elif not message.reply_to_message:
        return message.from_user.id
    else:
        return message.reply_to_message.from_user.id