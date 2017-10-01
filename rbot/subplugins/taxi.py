command = "!taxis"

taxis = ["D9 Taxi | 01 842 5555", "Lynk | 01 473 11 22", "NRC | 01 677 22 22"]

def main(rbot, author_id, message, thread_id, thread_type, **kwargs):
    rbot.sendMessage("\n".join([taxi for taxi in taxis]), thread_id=thread_id, thread_type=thread_type)
