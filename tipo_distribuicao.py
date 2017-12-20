from enum import Enum
import numpy as np
import random

class TipoDistribuicao(Enum):
	UNIFORME = 1
	EXPOENCIAL = 2
	NORMAL = 3

class Distribuicao(object):
	
	def __init__(self, tipo, params):
		self.tipo = tipo
		self.params = params
		
	def sample(self):

		if self.tipo == TipoDistribuicao.UNIFORME:
			inf, sup = self.params
			dist = random.uniform(inf, sup)

		elif self.tipo == TipoDistribuicao.EXPOENCIAL:
			lambd = 1.0 / self.params[0]
			dist = random.expovariate(lambd)

		elif self.tipo == TipoDistribuicao.NORMAL:
			media, desvio_padra = self.params
			dist = random.normalvariate(media, desvio_padra)

		return dist