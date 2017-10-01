command = "!help"

def main(rbot, author_id, message, thread_id, thread_type, **kwargs):
    rbot.sendMessage("The commands are: !egg, !bus <stopid>, !isonline, !taxis", thread_id=thread_id, thread_type=thread_type)
