# Se requiere implementar un grafo para almacenar las siete maravillas Arquitectonicas modernas y Naturales de mundo, para lo cual se deben tener en cuenta las siguientes actividades:
# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de uno en las Naturales) y tipo (Natural o Arquitectonica); DONE! 
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar la distancia que las separa; DONE! 
# c. hallar el árbol de expansion mínimo de cada tipo de las maravillas; DONE! 
# d. determinar si existen países que dispongan de maravillas Arquitecónicas y Naturales; DONE! 
# e. determinar si algún país tiene más de una maravilla del mismo tipo; DONE!
# f. deberá utilizar un grafo no dirigido. DONE! 


from grafo import Grafo
from random import randint

mi_grafo = Grafo(dirigido=False)

class Maravilla:
    
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo
    
    def __str__(self):
        return f'{self.nombre} - {self.pais} - {self.tipo}'

# Maravillas arquitectonicas:     
mi_grafo.insert_vertice(Maravilla("Gran Muralla", 'China', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Machu Picchu", 'Tanzania', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Petra", 'Jordania', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Monumento a la Bandera", 'Argentina', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Taj Mahal", 'India', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Coliseo", 'India', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Catedral de Santa María", 'España', 'Arquitectonica'), criterio='nombre')

# Maravillas naturales:
mi_grafo.insert_vertice(Maravilla("Cataratas del Iguazú", 'Argentina','Natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Gran Cañón", 'Estados Unidos', 'Natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Monte Everest", ['Nepal', 'Filipinas'], 'Natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Monte Kilimanjaro", 'Tanzania', 'Natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Bahía de Ha Long", 'Vietnam', 'Natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Parque Nacional de Plitvice", 'Croacia', 'Natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Auroras Boreales", ['Varios países en el Círculo Polar Ártico'],'Natural'), criterio='nombre')

# Insersiones arquitectonicas:
mi_grafo.insert_arist('Gran Muralla', 'Machu Picchu', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Gran Muralla', 'Petra', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Gran Muralla', 'Monumento a la Bandera', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Gran Muralla', 'Taj Mahal', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Gran Muralla', 'Coliseo', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Gran Muralla', 'Catedral de Santa María', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Machu Picchu', 'Petra', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Machu Picchu', 'Monumento a la Bandera', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Machu Picchu', 'Taj Mahal', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Machu Picchu', 'Coliseo', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Machu Picchu', 'Catedral de Santa María', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Petra', 'Monumento a la Bandera', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Petra', 'Taj Mahal', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Petra', 'Coliseo', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Petra', 'Catedral de Santa María', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Monumento a la Bandera', 'Taj Mahal', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Monumento a la Bandera', 'Coliseo', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Monumento a la Bandera', 'Catedral de Santa María', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Taj Mahal', 'Coliseo', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Taj Mahal', 'Catedral de Santa María', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Coliseo', 'Catedral de Santa María', randint(0, 1000), criterio_vertice='nombre')


# Insesiones naturales: 

mi_grafo.insert_arist('Cataratas del Iguazú', 'Gran Cañón', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Cataratas del Iguazú', 'Monte Everest', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Cataratas del Iguazú', 'Monte Kilimanjaro', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Cataratas del Iguazú', 'Bahía de Ha Long', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Cataratas del Iguazú', 'Parque Nacional de Plitvice', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Cataratas del Iguazú', 'Auroras Boreales', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Gran Cañón', 'Monte Everest', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Gran Cañón', 'Monte Kilimanjaro', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Gran Cañón', 'Bahía de Ha Long', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Gran Cañón', 'Parque Nacional de Plitvice', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Gran Cañón', 'Auroras Boreales', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Monte Everest', 'Monte Kilimanjaro', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Monte Everest', 'Bahía de Ha Long', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Monte Everest', 'Parque Nacional de Plitvice', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Monte Everest', 'Auroras Boreales', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Monte Kilimanjaro', 'Bahía de Ha Long', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Monte Kilimanjaro', 'Parque Nacional de Plitvice', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Monte Kilimanjaro', 'Auroras Boreales', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Bahía de Ha Long', 'Parque Nacional de Plitvice', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Bahía de Ha Long', 'Auroras Boreales', randint(0, 1000), criterio_vertice='nombre')
mi_grafo.insert_arist('Parque Nacional de Plitvice', 'Auroras Boreales', randint(0, 1000), criterio_vertice='nombre')

#mi_grafo.barrido()


# ori = 'Gran Muralla'
# des = 'Petra'
# origen = mi_grafo.search_vertice(ori, criterio='nombre')
# destino = mi_grafo.search_vertice(des, criterio='nombre')
# camino_mas_corto = None
# if(origen is not None and destino is not None):
#     if(mi_grafo.has_path(ori, des, criterio='nombre')):
#         camino_mas_corto = mi_grafo.dijkstra(ori, des)
#         fin = des
#         while camino_mas_corto.size() > 0:
#             value = camino_mas_corto.pop()
#             if fin == value[0]:
#                 print(value[0], value[1])
#                 fin = value[2]
# a = input()


def ejercicio_c():  
    bosque = mi_grafo.kruskal()
    for arbol in bosque:
        print('arbol')
        for nodo in arbol.split(';'):
            print(nodo)

def ejercicio_d():
    mi_grafo.barrido_desigual_tipo()

def ejercidio_e():
    mi_grafo.barrido_mismo_tipo()

ejercidio_e()