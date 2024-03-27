num = int(input("Digite um número: "))

primos = []

for i in range(2, num):
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
            break
        if primo and i not in primos:
            primos.append(i)

if primos:
    print("O número {} não é primo".format(num))
    print("Os números primos anteriores a ele são: {}".format(primos))
else:
    print("O número {} é primo".format(num))
    print("Os números primos anteriores a ele são: {}".format(primos))