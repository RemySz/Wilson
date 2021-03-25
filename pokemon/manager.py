import json, datetime
import os 
default_profile = {
	"pokemon": [],
	"name": "",
	"creation date": "",
	"id": 0
}

def CreateProfile(name: str, id_code: int):
	profile = default_profile
	profile["name"] = name
	profile["id"] = id_code
	profile["creation"] = datetime.datetime.now()

	with open("pokemon/data/users/{id}", 'w') as f:
		json.dump(profile, fp=f, sort_keys=True, indent=2)

def AddPokemonToProfile(id_code, pokemon: list = []):
	profile: dict = {}
	with open("pokemon/data/users/{id}", 'r') as f:
		profile=json.load(fp=f)
		for poke in pokemon:
			profile["pokemon"].append(poke)

	with open("pokemon/data/users/{id}", 'w') as f:
		json.dump(profile, fp=f, sort_keys=True, indent=2)


def Search(id_code: int, path="/pokemon/data/users/"):
	for root, dirs, files in os.walk(path):
		if id_code in files:
			return os.path.join(root, id_code)	


		
