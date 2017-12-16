from tipo_distribuicao import TipoDistribuicao
from gerador import GeradorChegada

class Escalonador(object):
    
    def __init__(self, tipo_distribuicao_chegada, params_distribuicao, tempo_medio_servico, duracao_simulacao, qnt_repeticoes):
        
        self.fila = []
        self.momemto = 0
        self.duracao_simulacao = duracao_simulacao
        self.tempo_medio_servico = tempo_medio_servico
        self.params_distribuicao = params_distribuicao
        self.set_tipo_distribuicao(tipo_distribuicao_chegada)

    def set_tipo_distribuicao(self, tipo_distribuicao_chegada):
    
        tipos_distribuicao = TipoDistribuicao()
        
        if tipo_distribuicao_chegada == 'uniforme':
            self.tipo_distribuicao_chegada = tipos_distribuicao.UNIFORME
        
        elif tipo_distribuicao_chegada == 'exponencial':
            self.tipo_distribuicao_chegada = tipos_distribuicao.EXPOENCIAL

        elif tipo_distribuicao_chegada == 'normal':
            self.tipo_distribuicao_chegada = tipos_distribuicao.NORMAL
            
    def run(self):
        
        gerador = GeradorChegada(self.tipo_distribuicao_chegada, self.tempo_medio_servico)

        while self.momemto <= self.duracao_simulacao:
            
            

            self.momemto = self.momemto + 1
    