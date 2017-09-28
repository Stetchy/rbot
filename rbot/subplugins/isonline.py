command = "!isonline"

def main(rbot, author_id, message, thread_id, thread_type, **kwargs):
	if rbot.ronline:
		rbot.sendMessage("I'm online, I will probably reply soon - bot pls", thread_id=thread_id, thread_type=thread_type)
	else:
		rbot.sendMessage("I'm actually not here and I'm definitely not ignoring you - bot pls", thread_id=thread_id, thread_type=thread_type)
