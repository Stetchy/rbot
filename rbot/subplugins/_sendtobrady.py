command = "!brady"

brady = "962153393855009"

def main(rbot, author_id, message, thread_id, thread_type, **kwargs):
    rbot.sendMessage(message, thread_id=brady, thread_type=thread_type)
