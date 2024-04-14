import classes
import random

def print_individuos(individuos):
    if not individuos:
        print("Lista de indivíduos vazia.")
        return

    for individuo in individuos:
        print(f"Individuo: {individuo}")

    print("\n")


def criar_individuos(num):
    novos_individuos = []
    for _ in range(num):
        novos_individuos.append(classes.INDIVIDUOS())

    return novos_individuos

def atualizar_individuos(num, velhos_individuos):
    novos_individuos = []
    velhos_individuos = tirar_randoms(velhos_individuos)
    i = 0
    while i != len(velhos_individuos):
        novos_individuos.append(velhos_individuos[i])
        i = i+1

    while i != num:
        novos_individuos.append(classes.INDIVIDUOS())
        i = i+1

    for individuo in novos_individuos:
        if individuo.get_x() == "random":
            individuo.set_x(random.uniform(-10, 10))

        if individuo.get_y() == "random":
            individuo.set_y(random.uniform(-10, 10))

    return novos_individuos

def tirar_randoms(individuos: list[classes.INDIVIDUOS]):
    individuos_a_remover = []
    i = 0
    for i in range(len(individuos)):
        if individuos[i].get_x() == "random" and individuos[i].get_y() == "random":
            individuos_a_remover.append(individuos[i])

    for individuo in individuos_a_remover:
        individuos.remove(individuo)

    return individuos

def criar_vet_strings(num):
    vetor_strings = []
    for i in range(num):
        vetor_strings.append("Individuo {}".format(i + 1))
    return vetor_strings