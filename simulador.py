from servidor import Servidor
from escalonador import Escalonador
from evento import Evento, TipoEvento


class Simulador(object):
    
    def __init__(self, tipo_distribuicao_chegada, params_distribuicao, tempo_medio_servico, duracao_simulacao, qnt_repeticoes):
        
        self.qnt_repeticoes = qnt_repeticoes        
        self.duracao_simulacao = duracao_simulacao
        self.tempo_medio_servico = tempo_medio_servico
        self.params_distribuicao = params_distribuicao
        self.tipo_distribuicao_chegada = tipo_distribuicao_chegada
        self.servidor = Servidor()
        self.escalonador = Escalonador(tipo_distribuicao_chegada, params_distribuicao, tempo_medio_servico, duracao_simulacao, qnt_repeticoes)
        self.req_recebidas = 0
        self.req_atendidas = 0

        
    def chegada(self):
    	req_recebidas += 1
    	fregues = Fregues()
    	e_chegada = Evento(TipoEvento.CHEGADA)
    	self.escalonador.escalonar(e_chegada,self.tipo_distribuicao_chegada) #Escalonar Chegada // É bom definir como deixar claro que é uma chegada
    	if (self.servidor.isLivre()):
    		self.servidor.ocupar()
    		e_termino = Evento(TipoEvento.TERMINO, fregues)
    		self.escalonador.escalonar(e_termino, DISTRIBUICAO_NAO_TEMOS_CERTEZA_AINDA) #Escalonar Termino
    	else:
    		e_enfileirar = Evento(TipoEvento.ENFILEIRAR, fregues)
    		self.escalonador.escalonar(, DISTRIBUICAO_NAO_TEMOS_CERTEZA_AINDA) #Colocar na Fila

    def termino(self, fregues):
    	req_atendidas += 1
    	fregues.finalizar()
    	if self.escalonar.fila.empty():
    		self.servidor.liberar()
    	else:
    		fregues_fila = self.escalonar.fila.get()
    		e_termino = Evento(TipoEvento.TERMINO, fregues_fila)
    		self.escalonador.escalonar(e_termino, TipoDistribuicao.EXPONENCIAL) # Escalonar Termino // Checar se é enum ou nao

    def enfileirar(self, fregues):
    	self.escalonador.fila.put(fregues); 

    def start(sef):
    	agenda = self.escalonador.agenda
    	while condicao:
    		ms = current_time()
    		if ms in agenda:
    			if agenda[ms] == Evento.CHEGADA:
    				self.chegada()
    			elif agenda[ms] == Evento.TERMINO:
    				self.termino(agenda[ms].fregues)
    			elif agenda[ms] == Evento.ENFILEIRAR:
    				self.enfileirar()


