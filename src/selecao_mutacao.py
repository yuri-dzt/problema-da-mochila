import random

def selecao_por_torneio(populacao, fitness_populacao, tamanho_torneio=3):
    torneio = random.sample(list(zip(populacao, fitness_populacao)), tamanho_torneio)
    return max(torneio, key=lambda x: x[1])[0]

def crossover(pai1, pai2):
    ponto = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

def mutacao(cromossomo, taxa_mutacao):
    for i in range(len(cromossomo)):
        if random.random() < taxa_mutacao:
            cromossomo[i] = 1 - cromossomo[i]
    return cromossomo
