import json 
import os 
import main

class Const(object):
	PATH_DATA: str = "../data/"


class Database:
	config = {
		"Active": True,
		"Datasets": [],
		"owner": main.bot.author
	}

	def __init__(self):
		json.dumps(Database.config, indent=2, path=Const.PATH_DATA)

	def save_dataset(dataset: object):
		json.dumps({"owner":dataset.owner,"data":dataset.data})

class Dataset:

	def __new__(cls):
		pass

	def __init__(self, data: list, owner: str):
		data: list = data
		owner: str = owner




	


