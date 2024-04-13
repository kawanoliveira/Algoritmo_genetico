import classes

def print_individuos(individuos):
    """
    Imprime todos os indivíduos da lista fornecida.

    Args:
        individuos (List[Individuo]): Lista de indivíduos a serem impressos.
    """

    if not individuos:
        print("Lista de indivíduos vazia.")
        return

    for individuo in individuos:
        print(f"Individuo: {individuo}")


def criar_individuos(num):
    novos_individuos = []
    for _ in range(num):
        novos_individuos.append(classes.INDIVIDUOS())

    return novos_individuos

def atualizar_lista(num, velhos_individuos):
    novos_individuos = []
    for _ in range(num):
        novos_individuos.append(classes.INDIVIDUOS())

    return novos_individuos

individuos = []

individuos = criar_individuos(int(input("Digite o número de indivíduos a serem criados: ")))

print_individuos(individuos)

segundo_individuo = individuos[1]
individuos.remove(segundo_individuo)
print("novos:")
print_individuos(individuos)