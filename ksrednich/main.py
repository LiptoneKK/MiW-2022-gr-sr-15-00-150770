import numpy as np
import pandas as pd
import math
import sklearn
import matplotlib as plt

#dystans euklidesowy
def distance(v1,v2):
    #jezeli grupa (cluster) jest pusty, to wtedy dystans jest nieskonczony
    if len(v1) == 0 or len(v2) == 0:
        return 1000
    sum = 0
    for i in range(len(v1)):
        sum += ((v2[i]-v1[i])**2)
    return math.sqrt(sum)


#rekurencyjna silnia (warunki: zdefiniowana tylko dla liczb dodatnich)
def factorial(n):
    if n < 0:
        return -1
    if n == 1 or n == 0:
        return 1
    return n*(factorial(n-1))


wlosy_kobiet = []
wlosy_mezczyzn = []

wzrost_kobiet = []
wzrost_mezczyzn = []

waga_kobiet = []
waga_mezczyzn = []


#przypisuje dlugosc wlosow k i m
for i in range(100):
    mu, sigma = 2.5, 0.8
    wlosy_k = np.random.normal(mu,sigma)
    wlosy_kobiet.append(wlosy_k)
    wlosy_m = np.random.normal(mu,sigma)
    wlosy_mezczyzn.append(wlosy_m)


#przypisuje wzrost i wage dla mezczyzn
for i in range(100):
    mu, sigma = 180, 7
    wzrost_m = np.round(np.random.normal(mu,sigma),0)
    wzrost_mezczyzn.append(wzrost_m)
    waga_m = np.round(wzrost_m - 100 + np.random.normal(0,5),0)
    waga_mezczyzn.append(waga_m)


#przypisuje wzrost i wage dla kobiet
for i in range(100):
    mu, sigma = 165, 5
    wzrost_k = np.round(np.random.normal(mu,sigma),0)
    wzrost_kobiet.append(wzrost_k)

    waga_k = np.round(wzrost_k - 100 + np.random.normal(0,12),0)
    waga_kobiet.append(waga_k)


#sprawdzam ile kobiet ma dlugie/srednie/krotkie wlosy
for n,i in enumerate(wlosy_kobiet):
    if i <= 2.0:
        i = 1
        wlosy_kobiet[n] = i
    elif i > 2.0 and i < 3:
        i = 2
        wlosy_kobiet[n] = i
    else:
        i = 3
        wlosy_kobiet[n] = i

#sprawdzam ile mezczyzn ma krotkie/srednie/dlugie wlosy
for n,i in enumerate(wlosy_mezczyzn):
    if i <= 2.0:
        i = 1
        wlosy_mezczyzn[n]=i
    elif i > 2.0 and i < 3:
        if np.random.uniform() < 0.8:
            i = 2
            wlosy_mezczyzn[n] = i
        else:
            i = 3
            wlosy_mezczyzn[n] = i
    else:
        i=3
        wlosy_mezczyzn[n] = i


#wyswietlam dane wejściowe
print('kobiet o krótkich włosach jest: {} '.format(str(wlosy_kobiet.count(1))))
print('kobiet o srednich włosach jest: {} '.format(str(wlosy_kobiet.count(2))))
print('kobiet o dlugich włosach jest: {} '.format(str(wlosy_kobiet.count(3))))

print('mezczyzn o krótkich włosach jest: {} '.format(str(wlosy_mezczyzn.count(1))))
print('mezczyzn o srednich włosach jest: {} '.format(str(wlosy_mezczyzn.count(2))))
print('mezczyzn o dlugich włosach jest: {} '.format(str(wlosy_mezczyzn.count(3))))


#tworze słownik potrzebny do df
etykieta_kobiet = ['Kobieta' for i in range(100)]
etykieta_mezczyzn = ['Mężczyzna' for i in range(100)]

dictionary = {'płeć': etykieta_kobiet+etykieta_mezczyzn,
              'wzrost': wzrost_kobiet+wzrost_mezczyzn,
              'waga': waga_kobiet+waga_mezczyzn,
              'długość włosów': wlosy_kobiet+wlosy_mezczyzn}

df = pd.DataFrame(dictionary)

#skalowanie danych
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df2 = df[['wzrost', 'waga', 'długość włosów']]
scaler.fit(df[['wzrost', 'waga', 'długość włosów']])
scaled_data = scaler.transform(df[['wzrost', 'waga', 'długość włosów']])

scaled_data_df = pd.DataFrame(data=scaled_data)

scaled_data_df

from sklearn.cluster import KMeans

kmeans = sklearn.cluster.KMeans(n_clusters=2).fit(scaled_data_df)
prediction = kmeans.labels_.astype(int)

#łączymy tabele
prediction_df = pd.DataFrame(data=prediction, columns=['klasyfikacja'])
df_full = pd.concat([df, scaled_data_df, prediction_df], axis=1)
df_full['klasyfikacja'] = np.where(df_full['klasyfikacja']==0, 1, 0)

print(df_full)
#mamy sklasyfikowana plec osoby po pozostałych parametrach
df_full.to_csv('k_means.csv')