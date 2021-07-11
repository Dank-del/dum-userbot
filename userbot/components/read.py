from userbot import botclient

def readCLI(chat: str):
    try:
        r = botclient.get_history(chat)
        c = botclient.get_chat(chat)
    except BaseException as e:
        print("Failed due to {}".format(e))
        return
    
    print(f'''Messages from {c.title} ~\nMessages arranged from newest to oldest.\n''')

    for i in r:
        try:
            if i.text:
                print(f'''{i.from_user.first_name} said "{i.text}"''')
            if i.photo:
                print(f'''{i.from_user.first_name} sent a photo {i.photo.file_id}''')
            if i.video:
                print(f'''{i.from_user.first_name} sent a video {i.video.file_id}''')
            if i.animation:
                print(f'''{i.from_user.first_name} sent a gif {i.animation.file_id}''')
            if i.document:
                print(f'''{i.from_user.first_name} sent a document {i.document.file_id}''')
            if i.voice:
                print(f'''{i.from_user.first_name} sent voice {i.voice.file_id}''')
            if i.location:
                print(f'''{i.from_user.first_name} sent location {i.location}''')
            if i.contact:
                print(chat, f'''{i.from_user.first_name} sent a contact {i.contact}''')
            if i.venue:
                print(chat, f'''{i.from_user.first_name} sent a venue {i.venue}''')
            if i.new_chat_member:
                print(chat, f'''{i.from_user.first_name} joined {i.new_chat_member.first_name}''')
            if i.left_chat_member:
                print(chat, f'''{i.from_user.first_name} left {i.left_chat_member.first_name}''')
            if i.audio:
                print(f'''{i.from_user.first_name} sent audio {i.audio.file_id}''')
        except BaseException as e:
            pass