import json
import requests

command = "!bus"

def get_json(stopid):
	return "http://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?stopid={:}&format=json".format(stopid)

def get_arrivals(url):
	arrivals = [{"arrivaldatetime": n["arrivaldatetime"].split(' ')[1], "route": n["route"]} for n in requests.get(url).json()['results']]
	return arrivals

def format_arrivals(arrivals):
	return [(n.get("arrivaldatetime"), n.get("route")) for n in arrivals]

def dbus_interface(stopid):
	return format_arrivals(get_arrivals(get_json(stopid)))

def prettify_info(message):
	records = dbus_interface(message)
	return '\n'.join([' | '.join(list(n)) for n in records])

def main(rbot, author_id, message, thread_id, thread_type, **kwargs):
	finished_records = prettify_info(message)
	if finished_records:
		rbot.sendMessage(finished_records, thread_id=thread_id, thread_type=thread_type)
	else:
		rbot.sendMessage("There are currently no routes listed at this stop, try again later.", thread_id=thread_id, thread_type=thread_type)
