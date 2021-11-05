import heapq as minheap
from tf_rutas_argentina import Grafo

class Dijkstra:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.visitados = {}
        self.ruta = []
        self.vertice_origen = None
        self.vertice_destino = None
        self.no_visitados = {v:[] for v in self.grafo.vertices()}

    def proximo_vertice (self): #-> Devuelve un vertice
        minheap.heapify()
        self.tabla_peso_ruta.values()