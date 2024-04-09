v = [9,8,7,12,0,13,21]

listaPar = []
listaImpar = []

for num in v:
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

print(listaPar)
print(listaImpar)