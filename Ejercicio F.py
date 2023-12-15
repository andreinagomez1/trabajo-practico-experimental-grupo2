import matplotlib.pyplot as plt
import networkx as nx

class Arbol:
    def __init__(self):
        self.G = nx.DiGraph()

    def agregar_nodo(self, padre, hijo):
        self.G.add_edge(padre, hijo)

    def mostrar(self):
        pos = {
            "Pablo": (1, 4),
            "Pedro": (0, 3),
            "Ramón": (2, 3),
            "Carlos": (-0.5, 2),
            "Pepe": (0.5, 2),
            "Aníbal": (1.5, 2),
            "Sandra": (2.5, 2),
            "Lady": (-0.93, 1),
            "Luis": (-0.16, 1),
            "Pamela": (0.10, 1),
            "Clara": (0.95, 1),
            "Inés": (1.70, 1),
            "Juan": (2.3, 1)
        }
        nx.draw(self.G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        plt.show()

# Creación del árbol
arbol = Arbol()

# Añadir los nodos y las aristas al árbol
arbol.agregar_nodo("Pablo", "Pedro")
arbol.agregar_nodo("Pablo", "Ramón")
arbol.agregar_nodo("Pedro", "Carlos")
arbol.agregar_nodo("Pedro", "Pepe")
arbol.agregar_nodo("Carlos", "Lady")
arbol.agregar_nodo("Carlos", "Luis")
arbol.agregar_nodo("Pepe", "Pamela")
arbol.agregar_nodo("Pepe", "Clara")
arbol.agregar_nodo("Ramón", "Aníbal")
arbol.agregar_nodo("Ramón", "Sandra")
arbol.agregar_nodo("Aníbal", "Inés")
arbol.agregar_nodo("Sandra", "Juan")

# Mostrar el árbol
arbol.mostrar()
