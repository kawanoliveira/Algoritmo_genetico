import random 
import math
import funcao_e_ranking as fk
import classes
import struct
    
def truncar_valor(valor):
    if valor > 10:
        return 10
    elif valor < -10:
        return -10
    else:
        return valor
    
def binario_para_float(binario):
    q = int(binario, 0)
    b8 = struct.pack('I', q)
    x = struct.unpack('f', b8)[0]
    return x

def float_para_binario(valor):
    binario = "0b"
    binario += bin(struct.unpack('!I', struct.pack('!f', valor))[0])[2:].zfill(32)

    return binario

def elitismo(vet):
    elite = []
    n = len(vet)
    x = math.ceil(n/100)
    for i in range(0,x):
        elite.append(vet[i])
    for i in range(0,x):
        del vet[0]
    
    return elite, vet

def ranking(vet):
    
    n = random.randint(1, len(vet))
    if n == 0:
        print("a")
    ranqueados = random.sample(vet, n)
    ranqueados = fk.selecaoRank(ranqueados)
    retornado = ranqueados[0]
    vet.remove(retornado)
    
        
    return retornado
    

def mutacao(indx, indy, muta):
    
    Xmutado = []
    Ymutado = []
    
    
    resultado = random.randrange(0, 100, 1)
    
    if resultado <= muta:
        Xmutado = ["0b"]
        for bit in indx[2:]:
            if bit == "1":
                Xmutado.append("0")
            else :
                Xmutado.append("1")
    else:
        Xmutado.append(indx)
        
    resultado = random.randrange(0, 100, 1)
    
    if resultado <= muta:
        Ymutado = ["0b"]
        for bit in indy[2:]:
            if bit == "1":
                Ymutado.append("0")
            else:
                Ymutado.append("1") 
    else:
        Ymutado.append(indy)
    
    Xmutado = ''.join(Xmutado)
    Ymutado = ''.join(Ymutado)
                
    x_mutado_float = binario_para_float(Xmutado)
    y_mutado_float = binario_para_float(Ymutado)
    
    # Truncar para o intervalo [-10, 10]
    x_mutado_float = truncar_valor(x_mutado_float)
    y_mutado_float = truncar_valor(y_mutado_float)
    
    # Converter de volta para binário
    Xmutado = float_para_binario(x_mutado_float)
    Ymutado = float_para_binario(y_mutado_float)
    
    return Xmutado, Ymutado


def cruzamento(pai1x, pai1y, pai2x, pai2y):

    Xdescendente = ""
    Ydescendente = ""
    for bit1, bit2 in zip(pai1x, pai2x):
        Xdescendente += random.choice([bit1, bit2])
    
    for bit1, bit2 in zip(pai1y, pai2y):
        Ydescendente += random.choice([bit1, bit2])

    # Converter de binário para inteiro
    x_descendente_float = binario_para_float(Xdescendente)
    y_descendente_float = binario_para_float(Ydescendente)
    
    # Truncar para o intervalo [-10, 10]
    x_descendente_float = truncar_valor(x_descendente_float)
    y_descendente_float = truncar_valor(y_descendente_float)
    
    # Converter de volta para binário
    Xdescendente = "0b"
    Xdescendente += bin(struct.unpack('!I', struct.pack('!f', x_descendente_float))[0])[2:].zfill(32)
    Ydescendente = "0b"
    Ydescendente += bin(struct.unpack('!I', struct.pack('!f', y_descendente_float))[0])[2:].zfill(32)

    return Xdescendente, Ydescendente
    
      
def cruzar_e_mutar(vetor_individuos, porcentagem_mutacao):
    
    novo_vetor = []

    elite, vetor_individuos = elitismo(vetor_individuos)
    for indiv in range(len(elite)):
        novo_vetor.append(elite[indiv])
    for indivduos in vetor_individuos:
        if len(vetor_individuos) != 1:
            ranqueado1 = ranking(vetor_individuos)
            ranqueado2 = ranking(vetor_individuos)
        
            filho1_x, filho1_y = cruzamento(ranqueado1.get_x(), ranqueado1.get_y(), ranqueado2.get_x(), ranqueado2.get_y())
            filho2_x, filho2_y = cruzamento(ranqueado1.get_x(), ranqueado1.get_y(), ranqueado2.get_x(), ranqueado2.get_y())
            filho1_x, filho1_y = mutacao(filho1_x, filho1_y, porcentagem_mutacao)
            filho2_x, filho2_y = mutacao(filho2_x, filho2_y, porcentagem_mutacao)
            novo_individuo = classes.INDIVIDUOS()
            novo_individuo.set_x(filho1_x)
            novo_individuo.set_y(filho1_y)
            novo_vetor.append(novo_individuo)
            novo_individuo.set_x(filho2_x)
            novo_individuo.set_y(filho2_y)
            novo_vetor.append(novo_individuo)

    return novo_vetor