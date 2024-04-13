import random


class INDIVIDUOS:

    def __init__(self, x="random", y="random"):
        self.x = None
        self.y = None
        self.fitness = None

        if x is None:   
            self.x = random.uniform(-10, 10)
        else:
            self.x = x
        
        if y is None:
            self.y = random.uniform(-10, 10)
        else:
            self.y = y

        self.fitness = "não determinado"

    def get_x(self):
        return self.x

    def set_x(self, novo_x):
        self.x = float(novo_x)

    def get_y(self):
        return self.y

    def set_y(self, novo_y):
        self.y = float(novo_y)

    def get_fitness(self):
        return self.fitness

    def set_fitness(self, novo_fitness):
        self.fitness = float(novo_fitness)

    def __str__(self):  # Define a string representation for better printing
        return f"Individuo: x={self.x:.3}, y={self.y:.3}, Fitness: {self.fitness}"