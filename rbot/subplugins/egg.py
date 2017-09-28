command = "!egg"

def main(rbot, author_id, message, thread_id, thread_type, **kwargs):
	rbot.sendMessage("🥚", thread_id=thread_id, thread_type=thread_type)