
def calculate_variance_population(use_dataset: bool = False, *args):
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
		VAR_X /= VAR_N
	return (f"ANSWER = {VAR_X}\nN = {VAR_N}\nMEW = {VAR_MEAN}\nSUM = {VAR_SUM}")

def calculate_variance_sample(use_dataset: bool = False, *args):
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