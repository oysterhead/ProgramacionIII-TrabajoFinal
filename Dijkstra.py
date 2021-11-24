import heapq as minheap
from tf_rutas_argentina import Grafo
import math

class Dijkstra:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.visitados = []
        self.tabla_peso = {v: (math.inf, None, None) for v in self.grafo.vertices()} #vertice:(infinito, vertice origen, iteracion) -> ojo: infinito es el peso pero al comienzo es infinito.
        self.priority_heap = [] #guardar (peso acum, vertex)
        self.iteracion = 0
        self.ruta = []
        self.peso_ruta = 0


    def calcular(self, origen: int, destino: int) -> list[int]:
        init_tag = (0, origen, self.iteracion)
        self.tabla_peso[origen] = init_tag
        minheap.heappush(self.priority_heap, init_tag)

        while not self.priority_heap == []:
            tag = minheap.heappop(self.priority_heap)
            peso_acum, vertice_actual = tag[0], tag[1]
            if vertice_actual not in self.visitados:
                self.iteracion +=1
                self.visitados.append(vertice_actual)

                for vecino in self.grafo.vecinos(vertice_actual):
                    if vecino not in self.visitados:
                        distancia_al_vecino = self.grafo.peso(vertice_actual, vecino)
                        peso_acum_vecino = self.tabla_peso[vecino][0]
                        nuevo_peso_acum_vecino = peso_acum + distancia_al_vecino
                        if nuevo_peso_acum_vecino < peso_acum_vecino:
                            self.tabla_peso[vecino] = (nuevo_peso_acum_vecino, vertice_actual, self.iteracion)
                            minheap.heappush(self.priority_heap, (nuevo_peso_acum_vecino, vecino))
        
        self.peso_ruta = self.tabla_peso[destino][0]
        vertex = destino
        while vertex != origen:
            self.ruta.append(vertex)
            vertex = self.tabla_peso[vertex][1]
        self.ruta.append(origen)

        return self.ruta[::-1] #ruta en orden de inicio a destino


if __name__ == "__main__":
    grafo = Grafo()
    grafo.agregarv(0)
    grafo.agregarv(5)
    grafo.agregara(0, 5, 13)
    origen = 0
    destino = 5
    grafo.agregarv(2)
    grafo.agregara(0, 2, 5)
    grafo.agregara(2, 5, 8)
    dj = Dijkstra(grafo)
    ruta = dj.calcular(origen, destino)
    peso = dj.peso_ruta
    print(peso)
    print(ruta)