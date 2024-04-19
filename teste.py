import matplotlib.pyplot as plt

# Dados do gráfico
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

# Criar figura e eixos
fig, ax = plt.subplots()

# Plotar dados
ax.plot(x, y)

# Ajustar o tamanho das bordas (espaço em branco) ao redor do gráfico
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.5)


# Exibir o gráfico
plt.show()