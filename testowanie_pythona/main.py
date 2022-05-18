print("Hello world")
znaki = "1234"
liczba = 6789

print("Najlepszym {} klubem na swiecie jest {}.".format("od konca","Stomil"))

print("{}, dolor sit amet, consectetur adipiscing elit. Etiam nisl sapien, eleifend et orci in, auctor commodo urna."
      .format("Lorem ipsum"))

print(type(znaki))
print(type(liczba))
print(type(2914.1741751762794908268296892))

str = "This article is written in {}"
print(str.format("Python"))


tab = ["ala","ma","kota","i","psa"]

print(" ".join(tab))

print("Ala ma kota i psa".split(" "))

zdanie = "Metody Inżynierii Wiedzy są najlepsze"
print(zdanie, len(zdanie))

print(zdanie.lower(), len(zdanie.lower()))

napis = zdanie.replace("ż", "z")
napis = napis.replace("ą", "a")
print(napis,len(napis))

y = set(napis)

print(y, len(y))

string = "ala"
lint = 12334


lista1 = [5,2,1,4]
lista2 = ["c","b","f"]

lista = lista1 + lista2
print(lista)

print(lista.index("c"))

imie = input("Jak masz na imie?")

print("Witaj, {}".format(imie))

x = [1,2,3]
print(x[0::1])
print(type(x[0::1]))
print(type(x[1]))

y = ["ala", "bartek", "monika", "tomasz"]

wynik = '_'.join(y)
print(wynik)

s = list(wynik.split("_"))
print(s)
dlugosc = "Metody Inżynierii Wiedzy są najlepsze"
print(len(dlugosc))

male = dlugosc.lower()
print(male)

zmienione = dlugosc.replace("ż", "z").replace("ą", "a")
print(zmienione)

v = set(zmienione)
print(v)
print(len(v))
string = "string"
integer = 6
trzy = 0
print((string, integer))
lista1 = ["ala", "magda"]
lista2 = ["tom", "Juan"]
print(lista1+lista2)
print(lista1.index("ala"))
lista1.append("Invader")
print(lista1)
lista1.insert(0, "Invader")
print(lista1)