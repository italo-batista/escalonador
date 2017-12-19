import numpy as np
import random

class TipoDistribuicao(enum):
    self.UNIFORME = 1
    self.EXPOENCIAL = 2
    self.NORMAL = 3

class Distribuicao(object):
	
	def __init__(self, tipo, media, params):
		self.tipo = tipo
		self.media = media
		self.params = params
		
	def gerar():

		if self.tipo == TipoDistribuicao.UNIFORME:
			low, high = params
			dist = random.uniform(low, high)

		elif self.tipo == TipoDistribuicao.EXPOENCIAL:
			lambd = params[0]
			dist = random.expovariate(lambd)

		elif self.tipo == TipoDistribuicao.NORMAL:
			mean, standard_deviation = params
			dist = random.normalvariate(mean, standard_deviation) 