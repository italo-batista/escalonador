
class TipoDistribuicao(enum):
    self.UNIFORME = 1
    self.EXPOENCIAL = 2
    self.NORMAL = 3

class Distribuicao(object):
	
	def __init__(self, tipo, media):
		self.tipo = tipo
		self.media = media

	#TO-DO
	def gerar():
		if self.tipo == TipoDistribuicao.UNIFORME:
			return 0 #eu nao sei se só o random funciona nesse caso

		elif self.tipo == TipoDistribuicao.EXPOENCIAL:
			return 0

		elif self.tipo == TipoDistribuicao.NORMAL:
			return 0


