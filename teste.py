import random

def ranking(vet):
    n = random.randint(0, len(vet) - 1)  # -1 para garantir que o índice esteja dentro dos limites
    ranqueados = random.sample(vet, n + 1)  # +1 para incluir o último elemento selecionado
    retornado = ranqueados[0]
    vet.remove(retornado)  # Remover o elemento selecionado da lista original
    return retornado

vetor = [1, 2, 3, 4, 5, 6, 7, 8]
print(ranking(vetor))
print(vetor)  # Mostrar a lista original após a remoção do elemento
