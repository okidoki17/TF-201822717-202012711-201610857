from weight_coordinates import get_value_longitud_trafico_segun_coordenadas
from weight_coordinates import transformToList
from weight_coordinates import set_peso_por_hora

# Rutas Mas Corta
def dijkstra(first, second, lista, type):
    queue = [[first, 0, first]]

    visited = [0] * len(lista)
    peso = [0] * len(lista)
    father = [-1] * len(lista)
    while queue:
        if type == "corto":
            [actual, pesoActual, fatherActual] = get_menor_value_queue(queue)
        elif type == "alter1":
            [actual, pesoActual, fatherActual] = get_mayor_value_queue(queue)
        elif type == "alter2":
            [actual, pesoActual, fatherActual] = get_ultimo_value_queue(queue)

        if visited[actual] == 0 and len(lista[actual][0]) > 0:
            visited[actual] = 1
            peso[actual] = pesoActual
            father[actual] = fatherActual
            
            set_append_segun_peso_corto(visited, actual, queue, lista, peso)
            if actual == second:
                fA = second
                listaFather = []
                listaFather.insert(0, fA)
                while fA != first:
                    fA = father[fA]
                    listaFather.insert(0, fA)


                return listaFather
                break


# obtener el menor de la lista
def get_menor_value_queue(queue):
    value = []
    menor = queue[0]
    if len(queue) > 1:
        for x in range(len(queue)):
            if menor[1] > queue[x][1]:
                menor = queue[x]
    value = menor
    queue.remove(menor)
    return value


def get_mayor_value_queue(queue):
    value = []
    mayor = queue[0]
    if len(queue) > 1:
        for x in range(len(queue)):
            if mayor[1] < queue[x][1]:
                mayor = queue[x]
    value = mayor
    queue.remove(mayor)
    return value


def get_ultimo_value_queue(queue):
    ultimo = queue[len(queue) - 1]
    value = ultimo
    queue.remove(ultimo)
    return value


def set_append_segun_peso_corto(visited, actual, queue, lista, peso):
    for i in range(len(lista[actual][0])):
        if visited[lista[actual][0][i][0]] == 0:
            queue.append([lista[actual][0][i][0],
                          peso[actual] + get_value_longitud_trafico_segun_coordenadas(lista[actual],
                                                                                      lista[lista[actual][0][i][0]],
                                                                                      lista[actual][0][i][1]), actual])


lista = transformToList()


def coords():
    aux=[]
    for i in lista:
        aux.append((i[1],i[2]))
    return aux

def list():
    aux=[]
    for i in lista:
        aux.append(i[0])
    return aux

coordGrafo=coords()
lista2=list()

set_peso_por_hora(lista, 1)
corto = dijkstra(1, 3, lista, "corto")
alt1 = dijkstra(1, 3, lista, "alter1")
alt2 = dijkstra(1, 3, lista, "alter2")

def graph():
    response = {"loc": coordGrafo, "g": lista2}
    return response

def paths():
    response = {"bestpath": corto, "path1": alt1, "path2": alt2}
    return response