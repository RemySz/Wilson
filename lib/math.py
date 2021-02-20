import numpy
from . import thread

@thread.RunInUniqueThread
def calculate_mean(use_dataset: bool = False, data: list = []):
	if use_dataset:
		pass
	length = len(data)
	sum_var = 0
	for i in data:
		sum_var += int(i)
	mean = sum_var/length
	return {"mean":mean,"sum":sum_var,"length":length}

@thread.RunInUniqueThread
def calculate_median(use_dataset: bool = False, data: list = []):
	data = numpy.sort(data)
	length = len(data)
	middle = length/2
	return {"median":middle,"length":length}

@thread.RunInUniqueThread
def calculate_variance_population(use_dataset: bool = False, data: list = []):
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
		DEVIATION = numpy.sqrt(VAR_X)
		return {"variance":VAR_X,'length':VAR_N,"mean":VAR_MEAN,"sum":VAR_SUM,"deviation":DEVIATION}

@thread.RunInUniqueThread
def calculate_variance_sample(use_dataset: bool = False, data: list = []):
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
		DEVIATION = numpy.sqrt(VAR_X)
		return {"variance":VAR_X,'length':VAR_N,"mean":VAR_MEAN,"sum":VAR_SUM,"deviation":DEVIATION}