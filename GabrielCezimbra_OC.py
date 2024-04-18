import struct
import random
import criarfilhos as cf
import classes

def funcao8(x, y):
    return (5 + (3*x) - (4*y) - (x**2) + (x*y) - (y**2))

#Calcular fitness de cada individuo da populacao
def FunFit(populacao):
    for INDVI in populacao:  
        x, y = decodeIndivi(INDVI)
        fitness = funcao8(x, y)  #Calcula o valor da funcao
        print(x, " ", y, " ", fitness)
        INDVI.set_fitness(fitness)

#Funcao para decodificar binario para real
def decodeIndivi(INDVI):
    q = int(INDVI.get_x(), 0)
    b8 = struct.pack('I', q)
    x = struct.unpack('f', b8)[0]
    q = int(INDVI.get_y(), 0)
    b8 = struct.pack('I', q)
    y = struct.unpack('f', b8)[0]

    return x, y

#Selecao dos pais com base no ranking
def selecaoRank(populacao):
    sortedPopulacao = sorted(populacao, key=lambda x: x.get_fitness(), reverse=True)
    return sortedPopulacao

#Mandei o GPT faze esse pedaco
populacao_size = 10
num_generations = 50
num_parents = 20

# Geração inicial da população
populacao = []

# Loop principal do algoritmo genético
for generation in range(num_generations):
    FunFit(populacao)
    # Seleção dos pais
    parents = selecaoRank(populacao)

    # Aplicação de cruzamento, mutação, etc. para gerar a próxima geração

# Após o término das iterações, você pode extrair o melhor indivíduo da última geração e decodificá-lo para obter os valores reais de x e y
best_INDVI = parents[0]
best_x, best_y = decodeIndivi(best_INDVI)
best_fitness = funcao8(best_x, best_y)

print("Melhor solução encontrada:"
      "\nx:", best_x,
      "\ny:", best_y,
      "\nFitness:", best_fitness)


