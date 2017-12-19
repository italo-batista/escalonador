from enum import Enum

class Evento(object):

	def __init__(self, tipo_evento, fregues=None):
		self.tipo_evento = tipo_evento
		self.fregues = fregues

class TipoEvento(Enum):
    CHEGADA = 1
    TERMINO = 2
    ENFILEIRAR = 3
        