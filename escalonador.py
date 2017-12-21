from Queue import Queue
from time_helper import current_time
from tipo_distribuicao import TipoDistribuicao, Distribuicao

class Escalonador(object):
    
    def __init__(self, tempo_medio_servico, servidor):
        
        self.fila = Queue()
        self.servidor = servidor
        self.tempo_medio_servico = tempo_medio_servico
        self.tempo_medio_atendendo = 0
        self.requisicoes_atendidas = 0
        self.qnt_media_elems_na_fila = 1.0
        self.distribuicao = Distribuicao(TipoDistribuicao.EXPOENCIAL, [self.tempo_medio_servico])

    def is_fila_vazia(self):
        return self.fila.empty()

    def enfileirar(self, fregues):
        self.fila.put(fregues)

    def atender_fregues_em_fila(self):
        fregues = self.fila.get()
        return self.escalonar(fregues)

    def escalonar(self, fregues):        
        self.servidor.ocupar()
        self.requisicoes_atendidas += 1
        tempo_para_termino = self.distribuicao.sample()
        fregues.finalizar(tempo_para_termino + current_time())
        self.__update_tempo_medio_atendendo(fregues)
        return tempo_para_termino + current_time()
    
    def __update_tempo_medio_atendendo(self, fregues):
        tempo_para_ser_atendido = fregues.get_tempo_para_ser_atendido()
        self.tempo_medio_atendendo = (
                self.tempo_medio_atendendo * (self.requisicoes_atendidas - 1) 
                + tempo_para_ser_atendido ) / (self.requisicoes_atendidas)

    def update_qnt_media_elems_na_fila(self, momento):
        self.qnt_media_elems_na_fila = (
                self.qnt_media_elems_na_fila * (momento) 
                + self.fila.qsize() ) / (momento + 1)

    def get_qnt_requisicoes_atendidas(self):
        return self.requisicoes_atendidas
	
    def get_tempo_medio_atendendo(self):
        return self.tempo_medio_atendendo

    def get_qnt_media_elems_na_fila(self):
        return self.qnt_media_elems_na_fila