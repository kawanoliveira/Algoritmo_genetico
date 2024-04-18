import random


def mutacao(indx, indy, muta):
    
    Xmutado = []
    Ymutado = []
    
    porcentagem = muta * 100
    
    resultado = random.randrange(0, 100, 1)
    
    if resultado <= porcentagem:
        
        for bit in indx:
            if bit == "1":
                Xmutado.append("0")
            else:
                Xmutado.append("1")
    else:
        Xmutado.append(indx)
        
    resultado = random.randrange(0, 100, 1)
    
    if resultado <= porcentagem:
        
        for bit in indy:
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

"""
pai1x = "1111111111"
pai1y = "0000000000"
pai2x = "1010101010"
pai2y = "0101010101"

resultadox, resultadoy = cruzamento(pai1x, pai1y, pai2x, pai2y)
print("Cromossomo x do filho: ", resultadox, "Cromossomo y do filho: ", resultadoy)

resultadox, resultadoy = mutacao(resultadox, resultadoy, 0.5)
print("Cromossomo x mutado: ", resultadox, "Cromossomo y mutado: ", resultadoy)

"""