# 14. Implementar sobre un grafo no dirigido los algoritmos necesarios para dar solución a las siguientes tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza y patio; DONE! 
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es de la distancia entre los ambientes, se debe cargar en metros; DONE!
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes; DONE! 
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para deteminar cuántos metros de cable de red se necesitan para conectar el router con el Smart TV. DONE! 

from grafo import Grafo

casa = Grafo(dirigido=False)

casa.insert_vertice('cocina')
casa.insert_vertice('comedor')
casa.insert_vertice('cochera')
casa.insert_vertice('quincho')
casa.insert_vertice('baño 1')
casa.insert_vertice('baño 2')
casa.insert_vertice('habitacion 1')
casa.insert_vertice('habitacion 2')
casa.insert_vertice('sala de estar')
casa.insert_vertice('terraza')
casa.insert_vertice('patio')

casa.insert_arist('cocina', 'comedor', 4)
casa.insert_arist('comedor', 'cochera', 6)
casa.insert_arist('cocina', 'cochera', 7)
casa.insert_arist('comedor', 'quincho', 3)
casa.insert_arist('baño 1', 'comedor', 6)
casa.insert_arist('quincho', 'baño 1', 5)
casa.insert_arist('habitacion 1', 'comedor', 7)
casa.insert_arist('habitacion 1', 'baño 2', 1)
casa.insert_arist('habitacion 2', 'baño 1', 1)
casa.insert_arist('sala de estar', 'quincho', 4)
casa.insert_arist('sala de estar', 'habitacion 1', 10)
casa.insert_arist('terraza', 'sala de estar', 1)
casa.insert_arist('terraza', 'quincho', 9)
casa.insert_arist('terraza', 'baño 1', 17)
casa.insert_arist('patio', 'cochera', 3)
casa.insert_arist('patio', 'cocina', 10)
casa.insert_arist('baño 2', 'cochera', 4)
casa.insert_arist('baño 2', 'patio', 11)
casa.insert_arist('habitacion 2', 'sala de estar', 9)
casa.insert_arist('habitacion 2', 'cocina', 7)
casa.insert_arist('sala de estar', 'patio', 20)

#casa.barrido()

#ejericio_c
def cantidad_cables():
    total_cables = 0
    bosque = casa.kruskal()
    for arbol in bosque:
        print('arbol total')
        for nodo in arbol.split(';'):
            partes = nodo.split('-')
            peso = int(partes[-1])
            total_cables += peso
    print(f'La longitud total de los cables necesarios es de: {total_cables} metros')

#cantidad_cables()          

def camino_mas_corto():
    ori = 'habitacion 1'
    des = 'sala de estar'
    origen = casa.search_vertice(ori)
    destino = casa.search_vertice(des)
    camino_mas_corto = None
    if(origen is not None and destino is not None):
        if(casa.has_path(ori, des)):
            camino_mas_corto = casa.dijkstra(ori, des)
            fin = des
            while camino_mas_corto.size() > 0:
                value = camino_mas_corto.pop()
                if fin == value[0]:
                    # print(value[0], value[1])
                    fin = value[2]
                    return value[1]
#casa.barrido()

metros = camino_mas_corto()

# ejercicio d

print(f'Se necesitan {metros} metros en total')