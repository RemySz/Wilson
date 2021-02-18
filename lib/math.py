
def calculate_variance_population_string(use_dataset: bool = False, data: list = []):
	if use_dataset:
		pass # TODO
	else: # data = [10, 10, 20]
		VAR_X = 0
		VAR_N = len(data) # N = 3
		VAR_SUM = 0
		for i in data:
			VAR_SUM += i # SUM = 40
		VAR_MEAN = VAR_SUM/VAR_N # MEAN = 40/3 = 13.33333334
		for i in data:
			term = i - VAR_MEAN # 10 - 13.333, 10 - 13.333, 20 - 13.333
			term = term ** 2
			VAR_X += term
		VAR_X /= VAR_N
		return (f"ANSWER = {VAR_X}\nN = {VAR_N}\nMEW = {VAR_MEAN}\nSUM = {VAR_SUM}")

def calculate_variance_population_raw(use_dataset: bool = False, data: list = []):
	if use_dataset:
		pass # TODO
	else: # data = [10, 10, 20]
		VAR_X = 0
		VAR_N = len(data) # N = 3
		VAR_SUM = 0
		for i in data:
			VAR_SUM += i # SUM = 40
		VAR_MEAN = VAR_SUM/VAR_N # MEAN = 40/3 = 13.33333334
		for i in data:
			term = i - VAR_MEAN # 10 - 13.333, 10 - 13.333, 20 - 13.333
			term = term ** 2
			VAR_X += term
		VAR_X /= VAR_N
		return {'answer':VAR_X,'n':VAR_N,"mean":VAR_MEAN,"sum":VAR_SUM}

def calculate_variance_sample_string(use_dataset: bool = False, *args):
	if use_dataset:
		pass # TODO
	else:
		dataset = [int(i) for i in args]
		VAR_X = 0
		VAR_N = len(dataset)
		VAR_SUM = 0
		for i in dataset:
			VAR_SUM += i
		VAR_MEAN = VAR_SUM/VAR_N
		for i in dataset:
			term = i - VAR_MEAN
		term = term ** 2
		VAR_X += term
		VAR_X /= VAR_N - 1
	return (f"ANSWER = {VAR_X}\nN = {VAR_N}\nMEW = {VAR_MEAN}\nSUM = {VAR_SUM}")

def calculate_variance_sample_raw(use_dataset: bool = False, data: list = []):
	if use_dataset:
		pass # TODO
	else:
		VAR_X = 0
		VAR_N = len(data)
		VAR_SUM = 0
		for i in data:
			VAR_SUM += i
		VAR_MEAN = VAR_SUM/VAR_N
		for i in data:
			term = i - VAR_MEAN
			term = term ** 2
			VAR_X += term
		VAR_X /= VAR_N - 1
	return {'answer':VAR_X,'n':VAR_N,"mean":VAR_MEAN,"sum":VAR_SUM}