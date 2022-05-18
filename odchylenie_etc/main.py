import numpy as np
import math as m
data = []
with open('Australian.dat', 'r') as plik:
    for wiersz in plik:
        data.append(list(map(lambda x: float(x), wiersz.split())))

lista = data
data = np.array(data)

def srednia_arytmetyczna(wiersz):
    suma = 0.0
    for i in wiersz:
        suma += i
    return float(suma / float(len(wiersz)))


def wariancja(wiersz):
    srednia = srednia_arytmetyczna((wiersz))
    suma = 0.0
    for i in wiersz:
        suma += (i-srednia)*(i-srednia)
    return suma / float(len(wiersz))


def odchylenie_standardowe(wiersz):
    return m.sqrt(wariancja(wiersz))


def srednia_arytmetyczna_macierz(macierz):
    return macierz.mean()


def wariancja_macierz(macierz):
    return macierz.var()


def odchylenie_standardowe_macierz(macierz):
    return macierz.std()


def sprawdz_wiersz(wiersz, wyswietlic = False):
    if(wyswietlic):
        print(wiersz)
    print("srednia arytmetyczna: ", srednia_arytmetyczna(wiersz))
    print("wariancja: ", wariancja(wiersz))
    print("odchylenie standardowe: ", odchylenie_standardowe(wiersz))


def sprawdz_macierz(macierz, wyswietlic = False):
    if(wyswietlic):
        print(macierz)
    print("srednia arytmetyczna: ", srednia_arytmetyczna_macierz(macierz))
    print("wariancja: ", wariancja_macierz(macierz))
    print("odchylenie standardowe: ", odchylenie_standardowe_macierz(macierz))


print("dla zerowego wiersza")
sprawdz_wiersz(lista[0], True)
print()
print("dla całej macierzy")
sprawdz_macierz(data)