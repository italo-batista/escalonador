
class Simulador(object):
    
    def __init__(self, tipo_distribuicao_chegada, params_distribuicao, tempo_medio_servico, duracao_simulacao, qnt_repeticoes):
        
        self.qnt_repeticoes = qnt_repeticoes        
        self.duracao_simulacao = duracao_simulacao
        self.tempo_medio_servico = tempo_medio_servico
        self.params_distribuicao = params_distribuicao
        self.tipo_distribuicao_chegada = tipo_distribuicao_chegada
