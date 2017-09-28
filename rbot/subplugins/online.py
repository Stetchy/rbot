command = "!online"

def main(rbot, author_id, message, thread_id, thread_type, **kwargs):
	rbot.ronline
	print(author_id)
	if str(author_id) == "100002203845098":
		rbot.ronline = not rbot.ronline
		rbot.sendMessage("status set to {:} {:}".format(rbot.ronline, "- bot pls"), thread_id=thread_id, thread_type=thread_type)
		return rbot.ronline