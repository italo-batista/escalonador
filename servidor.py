class Servidor(object):
    
    def __init__(self):
        self.estado = True

    def isLivre(self):
    	return self.estado

    def liberar(self):
    	self.estado = True

   	def ocupar(self):
   		self.estado = False
       