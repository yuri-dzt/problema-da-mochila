from algoritmo_genetico import algoritmo_genetico

pesos_e_valores = [
    [2, 10], [4, 30], [6, 300], [8, 10], 
    [8, 30], [8, 300], [12, 50], [25, 75], 
    [50, 100], [100, 400]
]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50

if __name__ == "__main__":
    melhores_individuos = algoritmo_genetico(
        pesos_e_valores, 
        peso_maximo, 
        tamanho_populacao=numero_de_cromossomos, 
        geracoes=geracoes
    )

    print("\nMelhores indivíduos por geração:")
    for i, (valor, individuo) in enumerate(melhores_individuos):
        print(f"Geração {i+1}: Valor = {valor}, Cromossomo = {individuo}")
