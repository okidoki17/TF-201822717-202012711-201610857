import math
from math import radians, sin, asin, sqrt, cos
import numpy as np
import heapq as hq
from random import randint
matrix = np.ones([12, 144])
matrixToList = np.ones([12, 144])
listToMatrix = []
hora = 0

lista = []


def removeEdgeMatrix(firstVertice, secondVertice):
    matrix[firstVertice][secondVertice] = 0


for i in range(18):
    for x in range(4, 12):
        removeEdgeMatrix(x, i)

for i in range(18, 29):
    for x in range(7, 12):
        removeEdgeMatrix(x, i)

for i in range(45, 97):
    for x in range(3, 6):
        removeEdgeMatrix(x, i)

for i in range(133, 144):
    removeEdgeMatrix(6, i)

sumaTotal = [0, 0]
verifiedY = 0


def get_value_cordenada(x, y):
    if sumaTotal[0] == 0 and sumaTotal[1] == 0:
        sumaTotal[0] = 40.831556
        sumaTotal[1] = 13.942969
    else:
        if x == 0:
            sumaTotal[0] = 40.831556
            sumaTotal[1] = 13.942969 + (10 * y)
        else:
            sumaTotal[0] = round(sumaTotal[0] + 10*7.2, 6)

            sumaTotal[1] = round(sumaTotal[1], 6)
    return sumaTotal


def transformToList():
    n = len(matrix) * len(matrix[0])
    sublist = []
    list = []
    posX = -1
    posY = 0

    for x in range(n):
        if posY < 144:
            if posX == 11:
                posY += 1
                posX = 0
            else:
                posX += 1
        else:
            break
        matrixToList[posX][posY] = x
        listToMatrix.append([posX, posY])

    posX = -1
    posY = 0

    for x in range(n):

        if posY < 144:
            if posX == 11:
                posY += 1
                posX = 0
            else:
                posX += 1
        if matrix[posX, posY] == 1:
            if 12 > posX >= 0 and 144 > posY - 1 >= 0:
                if matrix[posX, posY - 1] == 1:
                    sublist.append((math.floor(matrixToList[posX, posY - 1]), 0))
            if 12 > posX + 1 >= 0 and 144 > posY >= 0:
                if matrix[posX + 1, posY] == 1:
                    sublist.append((math.floor(matrixToList[posX + 1, posY]), 0))
            if 12 > posX >= 0 and 144 > posY + 1 >= 0:
                if matrix[posX, posY + 1] == 1:
                    sublist.append((math.floor(matrixToList[posX, posY + 1]), 0))
            if 12 > posX - 1 >= 0 and 144 > posY >= 0:
                if matrix[posX - 1, posY] == 1:
                    sublist.append((math.floor(matrixToList[posX - 1, posY]), 0))

        coords = get_value_cordenada(listToMatrix[x][0], listToMatrix[x][1])
        list.append([sublist, coords[0], coords[1]])
        sublist = []

    return (list)


def set_peso_por_hora(list, hora):
    for i in range(len(list)):
        for z in range(len(list[i][0])):
            list[i][0][z] = [list[i][0][z][0], 0]

    for i in range(len(list)):
        for z in range(len(list[i][0])):
            if z > 0:
                if 6 <= hora <= 12:
                    if list[i][0][z][1] == 0:
                        number = list[i][0][z][0]
                        for s in range(len(list[number][0])):
                            if i == list[number][0][s][0]:
                                list[i][0][z] = [list[i][0][z][0], randint(4, 8)]
                                list[number][0][s] = [list[number][0][s][0], list[i][0][z][1]]
                if 13 <= hora <= 18:
                    if list[i][0][z][1] == 0:
                        number = list[i][0][z][0]
                        for s in range(len(list[number][0])):
                            if i == list[number][0][s][0]:
                                list[i][0][z] = [list[i][0][z][0], randint(5, 9)]
                                list[number][0][s] = [list[number][0][s][0], list[i][0][z][1]]
                if 19 <= hora <= 24:
                    if list[i][0][z][1] == 0:
                        number = list[i][0][z][0]
                        for s in range(len(list[number][0])):
                            if i == list[number][0][s][0]:
                                list[i][0][z] = [list[i][0][z][0], randint(7, 10)]
                                list[number][0][s] = [list[number][0][s][0], list[i][0][z][1]]
                if 1 <= hora <= 5:
                    if list[i][0][z][1] == 0:
                        number = list[i][0][z][0]
                        for s in range(len(list[number][0])):
                            if i == list[number][0][s][0]:
                                list[i][0][z] = [list[i][0][z][0], randint(1, 4)]
                                list[number][0][s] = [list[number][0][s][0], list[i][0][z][1]]
def get_value_longitud_trafico_segun_coordenadas(coord_1, coord_2, trafic):
    def haversine(lon1, lat1, lon2, lat2):
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371
        return c * r

    return round(haversine(coord_1[1], coord_1[2], coord_2[1], coord_2[2]) * trafic, 6)