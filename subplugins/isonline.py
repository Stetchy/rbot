import online

command = "!online"

def main(rbot, text, thread_id, thread_type, **kwargs):
	if online.ronline:
		rbot.sendMessage("I'm online, I will probably reply soon", thread_id=thread_id, thread_type=thread_type)
	else:
		rbot.sendMessage("I'm actually not here and I'm definitely not ignoring you", thread_id=thread_id, thread_type=thread_type)
