from time_helper import current_time

class Fregues(object):
	
	def __init__(self):
		self.chegada = current_time()
		self.termino = -1

	def finalizar(self, termino):
		self.termino = termino
	
	def get_tempo_para_ser_atendido(self):
		return self.termino - self.chegada