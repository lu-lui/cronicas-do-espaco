class Grafos:
    def __init__(self):
        self.planetas = {}
        self.adjacencia = {}

    def add_vertice(self, planeta):
        self.planetas[planeta.name] = planeta
        self.adjacencia[planeta.name] = {}

    def add_aresta(self, origem, destino, peso):
        self.adjacencia[origem][destino] = peso
        self.adjacencia[destino][origem] = peso