import heapq as minheap
from tf_rutas_argentina import Grafo

'''
    c=v # vértice que estoy visitando
    visitados = [] # conjunto de vértices visitados
  anterior = {} # va guardadndo cual es el anterior de vada vertice en el camino de coste minimo
  distancia_acumulada= {} # valor de distancia desde el origen hasta cada vertice
  n = g.cantidad_vertices() # cantidad de vértices de mi grafo
  for j in g.vertices(): #por cada vertice de mi grafo
    distancia_acumulada.append(inf) # si no existe la arista se agrega infinito como peso
  distancia_acumulada[v] = 0
  for i in range (n-2): #cantidad de vertices - 2 (es decir sin contar vertice de origen ni destino) 
    c:= e not in visitados and sea el min distancia_acumulada[e] # tomo vertice que este mas cerca del origenque todavia no haya
    visitados.append(c) #marco c como visitado
    for j not in visitados: # para cada vertice no visitado
      if  distancia_acumulada[c]+g.peso(c,j) < distancia_acumulada[j]:
        distancia_acumulada[j] = distancia_acumulada[c]+g.peso(c,j) # cálculo de nuevo el peso del camino
        anterior[j] = c 
return distancia_acumulada, #usar la lsita de anteriores para reconstruir el camino. 
'''

'''
def dijkstra(self, start_vertex):
        etiquetas = {v:float('inf') for v in range(self.v)}
        etiquetas[start_vertex] = 0 #peso de vertex

        cola_prioridad = PriorityQueue()
        cola_prioridad.put((0, start_vertex))

        while not cola_prioridad.empty():
            (dist, current_vertex) = cola_prioridad.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D
'''

class Dijkstra:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.visitados = []
        self.tabla_peso = {v: (float('inf')) for v in self.grafo.vertices()} # ( peso acum, origen, iter)
        self.priority_heap = [] #guardar (peso acum, vertex)
        self.iteracion = 0
        self.ruta = []
        self.peso_ruta = 0


    def calcular(self, origen: int, destino: int) -> list(int):
        init_tag = (0,origen,self.iteracion)
        self.tabla_peso[origen] = init_tag
        minheap.heappush(self.priority_heap, init_tag)

        while not self.priority_heap == []:
            (peso_acum, vertice_actual) = minheap.heappop()
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
        
        return self.ruta[::-1] #ruta en orden de inicio a destino


if __name__ == "__main__":
    grafo = Grafo()
    dj = Dijkstra(grafo)
    origen = 0
    destino = 5
    ruta = dj.calcular(origen, destino)