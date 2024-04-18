import classes
import random
import struct

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
        if individuo.get_x() == "randomico":
            k = 0
            while k < 10:
                numero_aleatorio = random.randint(0, 2**32 - 1)
                binario = format(numero_aleatorio, '032b')
                binario_string = str(binario)
                binario_final = "0b"
                binario_final += binario_string
                
                q = int(binario_final, 0)
                b8 = struct.pack('I', q)
                x = struct.unpack('f', b8)[0]
                if x < 10 and x > -10:
                    k = 11
            individuo.set_x(binario_final)
        else:
            numero_float = float(individuo.get_x())
            binario = "0b"
            binario += bin(struct.unpack('!I', struct.pack('!f', numero_float))[0])[2:].zfill(32)
            individuo.set_x(binario)

        if individuo.get_y() == "randomico":
            k = 0    
            while k <= 10:
                numero_aleatorio = random.randint(0, 2**32 - 1)
                binario = format(numero_aleatorio, '032b')
                binario_string = str(binario)
                binario_final = "0b"
                binario_final += binario_string

                q = int(binario_final, 0)
                b8 = struct.pack('I', q)
                x = struct.unpack('f', b8)[0]
                if x < 10 and x > -10:
                    k = 11
            individuo.set_y(binario_final)
        else:
            numero_float = float(individuo.get_y())
            binario = "0b"
            binario += bin(struct.unpack('!I', struct.pack('!f', numero_float))[0])[2:].zfill(32)
            individuo.set_y(binario)

    return novos_individuos

def tirar_randoms(individuos: list[classes.INDIVIDUOS]):
    individuos_a_remover = []
    i = 0
    for i in range(len(individuos)):
        if individuos[i].get_x() == "randomico" and individuos[i].get_y() == "randomico":
            individuos_a_remover.append(individuos[i])

    for individuo in individuos_a_remover:
        individuos.remove(individuo)

    return individuos

def criar_vet_strings(num):
    vetor_strings = []
    for i in range(num):
        vetor_strings.append("Individuo {}".format(i + 1))
    return vetor_strings