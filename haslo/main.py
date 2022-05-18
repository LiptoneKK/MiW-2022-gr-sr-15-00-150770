lista = [1, 5, 0, 7, 7, 0]
print(lista)
lista.append(5)
print(lista)
lista.extend([5, 4, 3, 2])
print(lista)


dict = {
    "imie": "dariusz",
    "nazwisko": "solis"
}

print(dict)
print(dict.keys())
print(dict.values())


print(bool())
print(bool(''))
print(bool(0))
print(bool(1))
print(bool('0'))
print(bool('1'))
print(bool([]))
print(bool([","]))


i = 0
while i < 23:
    print(i)
    i += 1

napis = "Ala ma kota a kot ma Ale"
temp = ""
lista = []
for i in napis:
    if i == " ":
        lista.append(temp)
        temp = ""

    temp = temp + i

lista.append(temp)
print(lista)


#haslo: min dl = 10, male i duze litery, min jeden !
def sprawdzenie_hasla(haslo):

    duza,wykrzyknik,mala = False,False,False
    if len(haslo) < 10:
        return False

    for i in haslo:
        if i >= 'A' and i <= 'Z':
            duza = True
        if i == "!":
            wykrzyknik = True
        if i >= 'a' and i <= 'z':
            mala = True

    if (duza and mala and wykrzyknik) == True:
        return True
    else:
        return False


print(sprawdzenie_hasla("Darek!zda"))
print(sprawdzenie_hasla("Darek!!zda"))

liczby = [8, 20, 31, 44, 99, 33, 55, 68]

for i in liczby:
    if i != 99:
        print(i)

i = 1
while i <= len(liczby):
    if liczby[i] == 99:
        print(i)
        break
    i += 1


plik = open("cos.txt", "r")
print(plik.read(), end='')

with open("cos.txt", "r") as file:
    for line in file:
        print(line, end='')

print(plik.readlines())

jezyki = ["html", "css", "php", "javascript", "python"]

with open("cos.txt", "w") as file:
    for line in jezyki:
        print(line, file=file)