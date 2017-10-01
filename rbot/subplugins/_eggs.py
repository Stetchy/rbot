command = "!eggs"

def main(rbot, author_id, message, thread_id, thread_type, **kwargs):
	for i in range(0,100):
		rbot.sendMessage("🥚", thread_id=thread_id, thread_type=thread_type)
