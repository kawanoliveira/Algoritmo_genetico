import random 
import math

    
def truncar_valor(valor):
    if valor > 10:
        return 10
    elif valor < -10:
        return -10
    else:
        return valor
    
def binario_para_float(binario):
    return float(binario[2:]) / 1000.0

def float_para_binario(valor):
    return "0b" + bin(int(valor * 1000))[2:]

def elitismo(vet):
    elite = []
    n = len(vet)
    x = math.ceil(n/100)
    vet = sorted(vet, reverse=True)
    for i in range(0,x):
        elite.append(vet[i])
    for i in range(0,x):
        del vet[0]
    
    return elite, vet

def ranking(vet):
    
    n = random.randint(0, len(vet))
    ranqueados = random.sample(vet, n)
    ranqueados = sorted(ranqueados, reverse=True)
        
    return ranqueados[0]
    

def mutacao(indx, indy, muta):
    
    Xmutado = ["0b"]
    Ymutado = ["0b"]
    
    
    resultado = random.randrange(0, 100, 1)
    
    if resultado <= muta:
        
        for bit in indx[2:]:
            if bit == "1":
                Xmutado.append("0")
            else :
                Xmutado.append("1")
    else:
        Xmutado.append(indx)
        
    resultado = random.randrange(0, 100, 1)
    
    if resultado <= muta:
        
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

    Xdescendente = '0b' + Xdescendente
    Ydescendente = '0b' + Ydescendente
    
    # Converter de binário para inteiro
    x_descendente_int = int(Xdescendente, 2)
    y_descendente_int = int(Ydescendente, 2)
    
    # Truncar para o intervalo [-10, 10]
    x_descendente_int = truncar_valor(x_descendente_int)
    y_descendente_int = truncar_valor(y_descendente_int)
    
    # Converter de volta para binário
    Xdescendente = bin(x_descendente_int)
    Ydescendente = bin(y_descendente_int)
    
    return Xdescendente, Ydescendente


