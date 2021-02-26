from data.stream import DataStructure

def correct_access_level(function_access_level, user_id):
	stream = DataStructure()
	if stream.load(user_id) != Exception:
		if int(stream.data['access_level']) <= function_access_level:
			return True
	return False