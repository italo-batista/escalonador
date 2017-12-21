# coding: utf-8
from tipo_distribuicao import TipoDistribuicao

def write_results(dist_chegada_enum, dist_params, tempo_medio_servico, duracao_simulacao,
	qnt_requisicoes_recebidas, qnt_requisicoes_atendidas, tempo_medio_atendimento, qnt_media_elementos_em_espera):
	
	write_to_txt(dist_chegada_enum, dist_params, tempo_medio_servico, 
		duracao_simulacao, qnt_requisicoes_recebidas, qnt_requisicoes_atendidas, 
		tempo_medio_atendimento, qnt_media_elementos_em_espera
	)

	write_to_csv(dist_chegada_enum, dist_params, tempo_medio_servico, 
		duracao_simulacao, qnt_requisicoes_recebidas, qnt_requisicoes_atendidas, 
		tempo_medio_atendimento, qnt_media_elementos_em_espera
	)



def write_to_txt(dist_chegada_enum, dist_params, tempo_medio_servico, duracao_simulacao,
	qnt_requisicoes_recebidas, qnt_requisicoes_atendidas, tempo_medio_atendimento, qnt_media_elementos_em_espera):
	
	dist_chegada = enum_to_tipo_distribuicao(dist_chegada_enum)
	params = get_params_distribuicao(dist_chegada_enum, dist_params)

	with open('dados/resultados.txt','ab') as arquivo:
		arquivo.write(
			"Distribuição de chegada: " + dist_chegada + "\n" +
			"Parametros: " + params + "\n" + 
			"Valor médio serviço passado: " + str(tempo_medio_servico) + "\n" + 
			"Duração da Simulação: " + str(duracao_simulacao) + "\n" + 
			"Quantidade de Requisições recebidas: " + str(qnt_requisicoes_recebidas) + "\n" +
			"Quantidade de Requisições atendidas: " + str(qnt_requisicoes_atendidas) + "\n" +
			"Tempo médio de atendimento: " + str(tempo_medio_atendimento) + "\n" +		
			"Quantidade média de elementos em espera: " + str(qnt_media_elementos_em_espera) +
			"\n\n"
		)

def write_to_csv(dist_chegada_enum, dist_params, tempo_medio_servico, duracao_simulacao,
	qnt_requisicoes_recebidas, qnt_requisicoes_atendidas, tempo_medio_atendimento, qnt_media_elementos_em_espera):

	file_name = get_csv_file_name(dist_chegada_enum)
	dist_chegada = enum_to_tipo_distribuicao(dist_chegada_enum)
	params = get_params_distribuicao_to_csv(dist_chegada_enum, dist_params)

	with open(file_name,'ab') as arquivo:
		arquivo.write(
			"%s,%.2f,%.2f,%.2f,%.2f,%.2f,%.3f,%s \n" % 
				(
					dist_chegada, float(tempo_medio_servico), float(duracao_simulacao), 
					float(qnt_requisicoes_recebidas), float(qnt_requisicoes_atendidas),
					float(tempo_medio_atendimento), float(qnt_media_elementos_em_espera),
					params				
				)
		)

def enum_to_tipo_distribuicao(dist_enum):
	
	map_dist_chegada = {TipoDistribuicao.UNIFORME:"Uniforme",
					TipoDistribuicao.EXPOENCIAL: "Exponencial",
					TipoDistribuicao.NORMAL: "Normal"
	}
	return map_dist_chegada[dist_enum]

def get_params_distribuicao(dist_enum, params):

	if dist_enum == TipoDistribuicao.UNIFORME:
		inf, sup = params
		params_string = "Limite inferior: %d, Limite superior: %d" % (inf, sup)
			  
	elif dist_enum == TipoDistribuicao.EXPOENCIAL:
		lambd = 1.0 / params[0]
		params_string = "Lambda: %.2f" % (lambd)
						
	elif dist_enum == TipoDistribuicao.NORMAL:
		media, desvio_padrao  = params
		params_string = "Média: %d, Desvio padrão: %d" % (media, desvio_padrao)
		
	return params_string

def get_params_distribuicao_to_csv(dist_enum, params):

	if dist_enum == TipoDistribuicao.UNIFORME:
		inf, sup = params
		return "%.2f,%.2f" % (inf, sup)
			  
	elif dist_enum == TipoDistribuicao.EXPOENCIAL:
		lambd = 1.0 / params[0]
		return "%.2f,NA" % (lambd)
						
	elif dist_enum == TipoDistribuicao.NORMAL:
		media, desvio_padrao = params
		return "%.2f,%.2f" % (media, desvio_padrao)

def get_csv_file_name(dist_enum):
	
	if dist_enum == TipoDistribuicao.UNIFORME:
		return "dados/resultados-uniforme.csv"
			  
	elif dist_enum == TipoDistribuicao.EXPOENCIAL:
		return "dados/resultados-exponencial.csv"
						
	elif dist_enum == TipoDistribuicao.NORMAL:
		return "dados/resultados-normal.csv"
