def calcular_valor_e_peso(individuo, pesos_e_valores):
    valor_total = sum(individuo[i] * pesos_e_valores[i][1] for i in range(len(individuo)))
    peso_total = sum(individuo[i] * pesos_e_valores[i][0] for i in range(len(individuo)))
    return valor_total, peso_total

def calcular_fitness(individuo, pesos_e_valores, peso_maximo):
    valor_total, peso_total = calcular_valor_e_peso(individuo, pesos_e_valores)
    if peso_total > peso_maximo:
        return 0  
    return valor_total
