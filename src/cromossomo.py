import random

def gerar_cromossomo(tamanho):
    return [random.randint(0, 1) for _ in range(tamanho)]

def gerar_populacao(tamanho_populacao, tamanho_cromossomo):
    return [gerar_cromossomo(tamanho_cromossomo) for _ in range(tamanho_populacao)]
