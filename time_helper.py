import time
def current_time():
	return lambda: int(round(time.time() * 1000))