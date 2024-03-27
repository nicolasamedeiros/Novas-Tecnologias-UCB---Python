num = int(input("Digite um número: "))

counter = 0
base = num

while base != 0:
    if num%base == 0:
        counter += 1
    base -= 1

if counter == 2:
    print("O número {} é primo".format(num))
else:
    print("O número {} não é primo".format(num))