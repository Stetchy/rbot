from fbchat import log, Client
from contextlib import suppress
import os
import cfg
import random
import requests
import sys
import threading
import imp

class RBot(Client):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.load_subplugins()

	def load_subplugins(self):
		self.subplugins = {}
		for file in os.listdir('subplugins'):
			path = os.path.join('subplugins', file)
			subp = imp.load_source(file, path)
			if subp.command:
				self.subplugins[subp.command.lower()] = subp.name
	@staticmethod
	def clean_command(text):
		if " " in text:
			command, message = text.split(" ", 1)
		else:
			command, message = text, ""
		return command.lower(), message

	def run_subplugin(self, author_id, text, thread_id, thread_type, **kwargs):
		command, message = self.clean_command(text)
		if command in self.subplugins:
			subplugin = self.plugins[command]
			thread = threading.Thread(target=subplugin.main, args=(self, author_id, text, thread_id, thread_type), kwargs=kwargs)
			thread.deamon = True
			thread.start()

	def onMessage(self, author_id, text, thread_id, thread_type, **kwargs):
		self.markAsDelivered(thread_id)
		if text.startswith("!"):
			self.markAsRead()
			self.run_subplugin(author_id, text, thread_id, thread_type, **kwargs)

if __name__ == '__main__':
	client = RBot(cfg.email, cfg.password)
	while True:
		with suppress(requests.exceptions.ConnectionError):
			client.listen()
