import math as m
import numpy as np
import random as rm

miasta = ['olsztyn', 'gdansk', 'warszawa', 'radom', 'sosnowiec']
wynik = list(map(lambda s: s[:3], miasta))


data = []
with open('Australian.dat', 'r') as plik:
    for wiersz in plik:
        data.append(list(map(lambda x: float(x), wiersz.split())))


def euclidean_metrics(v1, v2):
    suma = 0
    for i in range(max(len(v1),len(v2))-1):
        suma+=(v1[i]-v2[i])**2
    return m.sqrt(suma)


############## W domu ################
# napisać funkcję która policzy odległosc kazdego objektu do objektu 0
# pogrupować wględem klasy decyzyjnej (ostatni atrybut) do słownika { klasa decyzyjna: lista wartosci}


def grouping_australians(lista,indeks_decyzja,obiekt_0):
    grupy = dict()
    y = lista[obiekt_0]
    for x in range(1,len(lista)):
        decyzyjna = lista[x][indeks_decyzja]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(euclidean_metrics(y, lista[x]))
        else:
            grupy[decyzyjna]=[euclidean_metrics(y, lista[x])]
    return grupy


#pogrupowani = grouping_australians(data,14,0)
#print(pogrupowani)


def k_nn(lista,indeks_decyzja,nowy_obiekt):
    grupy = dict()
    for x in range(0,len(lista)):
        decyzyjna = lista[x][indeks_decyzja]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(euclidean_metrics(nowy_obiekt, lista[x]))
        else:
            grupy[decyzyjna]=[euclidean_metrics(nowy_obiekt, lista[x])]
    return grupy


#print(k_nn(data,14,[1,1,1,1,1,1,1,1,1,1,1,1,1,1]))


def list_of_k_nn(lista,indeks_decyzja,nowy_obiekt):
    grupy = []
    for x in range(0,len(lista)):
        decyzyjna = lista[x][indeks_decyzja]
        grupy.append((decyzyjna,euclidean_metrics(nowy_obiekt, lista[x])))
    return grupy


#print(list_of_k_nn(data,14,[1,1,1,1,1,1,1,1,1,1,1,1,1,1]))


def grouping(lista, k):
    grupy = dict()
    for element in lista:
        decyzyjna = element[0]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(element[1])
        else:
            grupy[decyzyjna]=[element[1]]
    for klucz in grupy.keys():
        grupy[klucz].sort()
    for klucz in grupy.keys():
        suma = 0
        for ele in grupy[klucz][:k]:
            suma+= ele
        grupy[klucz]=suma
    return grupy


#print(grouping(list_of_k_nn(data, 14, [1,1,1,1,1,1,1,1,1,1,1,1,1,1]),5))


############## W domu ################
# funkcja minimum odległości do klasy

def minimum(slownik):
    klucze = list(slownik.keys())
    ilosc = 1
    klasa = klucze[0]
    minimum = slownik[klucze[0]]
    for key in klucze[1:]:
        if minimum > slownik[key]:
            minimum = slownik[key]
            klasa = key
            ilosc=1
        elif minimum == slownik[key]:
            ilosc+=1
    if ilosc > 1:
        return
    return klasa