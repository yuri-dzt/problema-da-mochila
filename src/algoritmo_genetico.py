from cromossomo import gerar_populacao
from fitness import calcular_fitness, calcular_valor_e_peso
from selecao_mutacao import selecao_por_torneio, crossover, mutacao

def algoritmo_genetico(
    pesos_e_valores, 
    peso_maximo, 
    tamanho_populacao=150,  
    geracoes=50,  
    taxa_mutacao=0.01  
):
    tamanho_cromossomo = len(pesos_e_valores)
    populacao = gerar_populacao(tamanho_populacao, tamanho_cromossomo)
    historico_melhores = []
    
    for geracao in range(geracoes):
        fitness_populacao = [calcular_fitness(individuo, pesos_e_valores, peso_maximo) for individuo in populacao]
        
        nova_populacao = []
        
        while len(nova_populacao) < tamanho_populacao:
            pai1 = selecao_por_torneio(populacao, fitness_populacao)
            pai2 = selecao_por_torneio(populacao, fitness_populacao)
                
            filho1, filho2 = crossover(pai1, pai2)
            filho1 = mutacao(filho1, taxa_mutacao)
            filho2 = mutacao(filho2, taxa_mutacao)
            nova_populacao.extend([filho1, filho2])
        
        populacao = nova_populacao[:tamanho_populacao]

        melhores_fitness = max(fitness_populacao)
        melhor_individuo = populacao[fitness_populacao.index(melhores_fitness)]
        melhor_valor, melhor_peso = calcular_valor_e_peso(melhor_individuo, pesos_e_valores)
        
        historico_melhores.append([melhor_valor, melhor_individuo])
        
        print(f"Geração {geracao+1} - Melhor valor: {melhor_valor}, Peso: {melhor_peso}")
    
    return historico_melhores
