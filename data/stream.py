class AccessLevel(object):
	Developer = 0
	Administrator = 1
	Moderator = 2
	Member = 3

class DataStructure:

	def __init__(self):
		self.data = {}
		self.user_id: int

	def load(self, user_id, additional_path_info=""):
		try:
			with open(f"{additional_path_info}data{user_id}.txt", 'r') as file: #739134752824754317
				info = file.readlines()

				for item in info:
					item = item.replace(' ','')
					item = item.replace('\n','')
					item = item.split(':')
					self.data[item[0]] = item[1]

				self.user_id = user_id
				
		except Exception as e:
			print(e)
			

	def dump(self, additional_path_info=""):
		try:
			output: str = ""
			print(self.data.items())
			for item in self.data.items():
				output += f"{item[0]}: {item[1]}\n"
			with open(f"{additional_path_info}data{self.user_id}.txt", 'w') as file:
				file.write(output)

		except Exception as e: 
			print(f"error {e}")

	def delete(self, user_id, additional_path_info=""):
		try:
			with open(f"{additional_path_info}/data{user_id}.txt", 'w') as file:
				file.write()
		except Exception:
			return Exception


	def clear(self):
		self.data = {}
		self.user_id = ""
