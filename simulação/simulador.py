# coding: utf-8
import time
from servidor import Servidor
from fregues import Fregues
from escalonador import Escalonador
from util.time_helper import current_time
from util.file_helper import write_results
from tipo_distribuicao import TipoDistribuicao, Distribuicao

import argparse
parser = argparse.ArgumentParser(description='Customize a execução de uma simulação')
parser.add_argument('--tipo-distribuicao', type=str, default='uniforme',
                        help='tipo de distribuição de chegada (opções: uniforme, normal, exponencial)')
parser.add_argument('--params-distribuicao', type=float, nargs='+', default=[0, 1],
                        help="""parâmetros específicos a depender do tipo de distribuição 
                        (ex: para uma distribuição uniforme cujor valor deve estar entre 0 e 1,
                        os parametros são 0 e 1).""")
parser.add_argument('--tmp-medio-servico', type=int, default=1, help='tempo medio de servico de um cliente em seg')
parser.add_argument('--tmp-simulacao', type=int, default=10, help='duracao total desejada para a simulação em seg')
parser.add_argument('--n-repeticoes', type=int, default=30, help='quantidade de repetições')


class Simulador(object):

    def __init__(self, tipo_distribuicao_chegada, params_distribuicao, tempo_medio_servico, duracao_simulacao, qnt_repeticoes):
        """
        Construtor.

        Args:
                tipo_distribuicao_chegada (TipoDistribuicao): Tipo de distribuição de propabilidade para chegada de clientes.			
                params_distribuicao (list): Lista com parâmetros da distribuição. Consulte doc de tipo_distribuicao.
                tempo_medio_servico (int): Tempo médio que um cliente dura no serviço, em segundos.
                duracao_simulacao (int): Tempo que uma simulação deve durar, em segundos.
                qnt_repeticoes (int): Quantidade de repetições de uma simulação.
        """

        self.qnt_repeticoes = qnt_repeticoes
        self.duracao_simulacao = duracao_simulacao
        self.tempo_medio_servico = tempo_medio_servico
        self.params_distribuicao = params_distribuicao
        self.tipo_distribuicao_chegada = tipo_distribuicao_chegada
        self.distribuicao = Distribuicao(self.tipo_distribuicao_chegada, self.params_distribuicao)

    def run(self):

        for repeticao in xrange(self.qnt_repeticoes):

            servidor = Servidor()
            escalonador = Escalonador(self.tempo_medio_servico, servidor)

            self.requisicoes_recebidas = 0
            self.tempo_inicio = current_time()
            proxima_chegada = int(current_time() + self.distribuicao.sample())
            proximo_termino = 0

            while(not self.fim_execucao(self.tempo_inicio)):

                if (current_time() >= proximo_termino):
                    servidor.liberar()

                if (servidor.is_livre()):
                    if (not escalonador.is_fila_vazia()):
                        proximo_termino = int(
                            escalonador.atender_fregues_em_fila())

                    elif (self.chegou_fregues(proxima_chegada)):
                        fregues = Fregues()
                        proxima_chegada = int(
                            current_time() + self.distribuicao.sample())
                        proximo_termino = int(escalonador.escalonar(fregues))

                else:
                    if (self.chegou_fregues(proxima_chegada)):
                        fregues = Fregues()
                        escalonador.enfileirar(fregues)

                escalonador.update_qnt_media_elems_na_fila(self.get_momento())
                time.sleep(0.9)

            write_results(
                self.tipo_distribuicao_chegada,
                self.params_distribuicao,
                self.tempo_medio_servico,
                self.duracao_simulacao,
                self.requisicoes_recebidas,
                escalonador.get_qnt_requisicoes_atendidas(),
                escalonador.get_tempo_medio_atendendo(),
                escalonador.get_qnt_media_elems_na_fila()
            )

    def fim_execucao(self, tempo_inicio):
        delta = current_time() - self.tempo_inicio
        return delta > self.duracao_simulacao

    def chegou_fregues(self, proxima_chegada):
        if current_time() >= proxima_chegada:
            self.requisicoes_recebidas += 1
            return True
        return False

    def get_momento(self):
        return current_time() - self.tempo_inicio


if __name__ == "__main__":    
    args = parser.parse_args()
    
    tipo_distribuicao = args.tipo_distribuicao
    params_distribuicao = args.params_distribuicao
    n_repeticoes = args.n_repeticoes
    tmp_medio_servico = args.tmp_medio_servico
    tmp_simulacao = args.tmp_simulacao

    if tipo_distribuicao == 'uniforme':
        sim = Simulador(TipoDistribuicao.UNIFORME, params_distribuicao, tmp_medio_servico, tmp_simulacao, n_repeticoes)
    elif tipo_distribuicao == 'normal':
        sim = Simulador(TipoDistribuicao.NORMAL, params_distribuicao, tmp_medio_servico, tmp_simulacao, n_repeticoes)
    elif tipo_distribuicao == 'exponencial':
        sim = Simulador(TipoDistribuicao.EXPONENCIAL, params_distribuicao, tmp_medio_servico, tmp_simulacao, n_repeticoes)
    else:
        raise SystemExit
    
    sim.run()
    