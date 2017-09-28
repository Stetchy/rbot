from fbchat import log, Client
from contextlib import suppress
import os
import cfg
import requests
import threading
import imp

class RBot(Client):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ronline = True
		self.load_subplugins()

	def load_subplugins(self):
		self.subplugins = {}
		for file in os.listdir('subplugins'):
			if not file.startswith("_"):
				path = os.path.join('subplugins', file)
				subp = imp.load_source(file, path)
				print(subp)
				if subp.command:
					self.subplugins[subp.command.lower()] = subp

	@staticmethod
	def clean_command(message):
		if " " in message:
			command, message = message.split(" ", 1)
		else:
			command, message = message, ""
		return command.lower(), message

	def run_subplugin(self, author_id, message, thread_id, thread_type, **kwargs):
		command, message = self.clean_command(message)
		if command in self.subplugins:
			subplugin = self.subplugins[command]
			print(subplugin)
			thread = threading.Thread(target=subplugin.main, args=(self, author_id, message, thread_id, thread_type), kwargs=kwargs)
			thread.deamon = True
			thread.start()

	def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
		self.markAsDelivered(author_id, thread_id)
		if message.startswith("!"):
			self.markAsRead(author_id)
			self.run_subplugin(author_id, message, thread_id, thread_type, **kwargs)
		if str(author_id) == "100003390970338":
			self.sendMessage("Go away dave", thread_id=thread_id, thread_type=thread_type)

if __name__ == '__main__':
	client = RBot(cfg.email, cfg.password)
	while True:
		with suppress(requests.exceptions.ConnectionError):
			client.listen()
