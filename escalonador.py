from tipo_distribuicao import TipoDistribuicao
from gerador import GeradorChegada
from time_helper import current_time
from Queue import Queue

class Escalonador(object):
    
    def __init__(self, tipo_distribuicao_chegada, params_distribuicao, tempo_medio_servico, duracao_simulacao, qnt_repeticoes):
        
        self.fila = Queue()
        self.agenda = {}
        self.momemto = current_time()
        self.tipo_distribuicao = tipo_distribuicao_chegada 
        self.params_distribuicao = params_distribuicao
        self.tempo_medio_servico = tempo_medio_servico
        self.duracao_simulacao = duracao_simulacao
        self.repeticoes = qnt_repeticoes

    #TO-DO: Passar pras distribuicoes os outros parametros se precisar
    def escalonar(self, evento, tipo_dist):
        dist = Distribuicao(tipo_dist, tempo_medio_servico)
        tempo = self.current_time() + dist.gerar()
        while(tempo in self.agenda):
            tempo = self.current_time() + dist.gerar()
        self.agenda[tempo] = evento
    