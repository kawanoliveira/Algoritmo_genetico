import random 
import math

    


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
                
    return ''.join(Xmutado),''.join(Ymutado)
        
        
        


def cruzamento(pai1x, pai1y, pai2x, pai2y):

    Xdecendente = []
    for bit1, bit2 in zip(pai1x, pai2x):
        bitDecendente = random.choice([bit1, bit2])
        Xdecendente.append(bitDecendente)
    
    Ydecendente = []  
    for bit1, bit2 in zip(pai1y, pai2y):
        bitDecendente = random.choice([bit1, bit2])
        Ydecendente.append(bitDecendente)

    return ''.join(Xdecendente),''.join(Ydecendente)


