from tipo_distribuicao import TipoDistribuicao
import random


class GeradorChegada(object):
	
	def __init__(self, tipo_distribuicao, tempo_medio_servico):
		self.tipo_distribuicao = tipo_distribuicao
		self.tempo_medio_servico = tempo_medio_servico

	def proxima_chegada(self, momento):
	   	
		tipos_distribuicao = TipoDistribuicao()

		if self.tipo_distribuicao == tipos_distribuicao.UNIFORME:
			return self.proxima_chegada_uniforme(momento)

		elif self.tipo_distribuicao == tipos_distribuicao.EXPOENCIAL:
			return self.proxima_chegada_exponencial(momento)

		elif self.tipo_distribuicao == tipos_distribuicao.NORMAL:
			return self.proxima_chegada_normal(momento)

	def proxima_chegada_uniforme(self, momento):
		tempo_chegada = momento + random.random() * self.tempo_medio_servico
		return tempo_chegada
	
	def proxima_chegada_exponencial(self, momento):
		return
	
	def proxima_chegada_normal(self, momento):
		return
	
