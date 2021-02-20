from threading import Thread
"""
	Simple threading wrapper

"""

def RunInUniqueThread(function, *args, **kwargs):
	def run():
		t = Thread(
			target=function(),
			args=args,
			kwargs=kwargs
		)
		t.start()
		return t
	return run

class ThreadQueue:
	"""
	Alternative to @RunInUniqueThread which maintains an active queue and
	executes them one after another.
	"""
	def __init__(self):
		self.queue = []

