import struct
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

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

def decodeNum(x):
    q = int(x, 0)
    b8 = struct.pack('I', q)
    x = struct.unpack('f', b8)[0]
    return x

#Selecao dos pais com base no ranking
def selecaoRank(populacao):
    sortedPopulacao = sorted(populacao, key=lambda x: x.get_fitness(), reverse=True)
    return sortedPopulacao

def executar_algoritmo(vetor_de_individuos,
                       bool_max_geracoes,
                       int_numero_max_geracoes,
                       bool_valor_alcancado,
                       float_valor_a_ser_alcancado,
                       bool_convergencia_prematura,
                       int_numero_para_convergencia_prematura,
                       float_porcentagem_de_mutacao,
                       janela):
    x_graph = []
    y_graph = []
    z_graph = []

    geracoes_sem_mudar = 0
    if bool_max_geracoes:
        for i in range(int_numero_max_geracoes):
            FunFit(vetor_de_individuos)
            vetor_de_individuos = selecaoRank(vetor_de_individuos)
            x_graph += [decodeNum(vetor_de_individuos[individuos].get_x()) for individuos in range(len(vetor_de_individuos))]
            y_graph += [decodeNum(vetor_de_individuos[individuos].get_y()) for individuos in range(len(vetor_de_individuos))]
            z_graph += [vetor_de_individuos[individuos].get_fitness() for individuos in range(len(vetor_de_individuos))]
    else:
        continuar = True
        while continuar:
            FunFit(vetor_de_individuos)
            vetor_de_individuos = selecaoRank(vetor_de_individuos)
            if bool_valor_alcancado:
                if vetor_de_individuos[0].get_fitness() >= float_valor_a_ser_alcancado:
                    continuar = False
            if bool_convergencia_prematura:
                if geracoes_sem_mudar == int_numero_para_convergencia_prematura:
                    continuar = False

    # Criar figura e eixos 3D
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')

    # Plotar pontos em 3D
    ax.scatter(x_graph, y_graph, z_graph, c='r', marker='o')

    # Definir rótulos dos eixos
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')

    # Definir cor de fundo
    fig.set_facecolor('#242424')
    ax.set_facecolor('#242424')
    ax.set_xlabel('Eixo X', color='blue')
    ax.set_ylabel('Eixo Y', color='green')
    ax.set_zlabel('Eixo Z', color='red')
    ax.tick_params(axis='x', colors='blue')
    ax.tick_params(axis='y', colors='green')
    ax.tick_params(axis='z', colors='red')
    ax.xaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
    ax.yaxis.set_pane_color((0.9, 0.9, 0.9, 1.0))
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.77, rely=0.7, anchor='center')