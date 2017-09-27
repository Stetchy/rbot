command = "!online"

ronline = True

def main(rbot, author_id, text, thread_id, thread_type, **kwargs):
	global online
	if author_id == "699671873449601":
		ronline = not ronline
		return ronline