from time_helper import current_time

class Fregues(object):
	def __init__(self):
		self.chegada = current_time()
		self.termino = -1

	def finalizar(self):
		self.termino = current_time()