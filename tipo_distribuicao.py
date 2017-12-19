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
			inf, sup = params
			dist = random.uniform(inf, sup)

		elif self.tipo == TipoDistribuicao.EXPOENCIAL:
			lambd = params[0]
			dist = random.expovariate(lambd)

		elif self.tipo == TipoDistribuicao.NORMAL:
			media, desvio_padra = params
			dist = random.normalvariate(media, desvio_padra)

		return dist