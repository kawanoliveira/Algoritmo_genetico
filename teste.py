
import random
import criarfilhos as cf
import classes

populacao_size = 10
num_generations = 50
num_parents = 20

# Geração inicial da população
populacao = []
for i in range(populacao_size):
    novoindiv = classes.INDIVIDUOS()
    novoindiv.set_fitness(i)

    populacao.append(novoindiv)

def selecaoRank(populacao):
    sortedPopulacao = sorted(populacao, key=lambda x: x.get_fitness(), reverse=True)
    return sortedPopulacao

x = selecaoRank(populacao)
print(x)