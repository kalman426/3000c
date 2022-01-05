lista = []

with open("input.txt", "r", encoding="utf8") as f:
    for i in f:
        lista.append(int(i))

print("masodik feladat")
m = 0
for count, i in enumerate(lista):

    if i%7 == 0:
        m=count
print(m)

print("negyedik feladat")

m = pow(sum(lista) % len(lista), 2)
print(m)

print("hatodik feladat")
m=0
for i in lista:
    if i % 9== 0:
        m+=1
print(m)

print("nyolcadik feladat")
print(len(lista))

print("tizedik feladat")
m = lista[0]
for i in lista[1:]:
    if i < m:
        m = i

print(m / 2)


