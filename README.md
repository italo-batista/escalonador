# Escalonador de 1 fila

Implementação de um escalonador de eventos com 1 fila, no contexto do problema de Fregueses de uma Barbearia.

É possível rodar uma simulação usando um dos três seguintes tipos de distribuição:

- uniforme
- normal
- expoencial

Para execução, você deve especificar, além do tipo de distribuição, outros parâmetros, como número de repetições ou tempo médio de serviço.

A seguir, exemplos de como executar o simulador considerando cada tipo de simulação:

### distribuição uniforme

```
python simulador.py --tipo-distribuicao uniforme --params-distribuicao 0 1 --tmp-medio-servico 1 --tmp-simulacao 10 --n-repeticoes 30
```

### distribuição normal

```
python simulador.py --tipo-distribuicao normal --params-distribuicao 0.5 0.4 --tmp-medio-servico 1 --tmp-simulacao 10 --n-repeticoes 30
```

### distribuição exponencial

```
python simulador.py --tipo-distribuicao exponencial --params-distribuicao 1 --tmp-medio-servico 1 --tmp-simulacao 10 --n-repeticoes 30
```

## instale as dependências

```
python -m pip  install numpy enum
```
