class Servidor(object):
	
	def __init__(self):
		self.livre = True

	def is_livre(self):
		return self.livre

	def liberar(self):
		self.livre = True
		
	def ocupar(self):
		self.livre = False
	   