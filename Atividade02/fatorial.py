num = int(input("Digite um número: "))

if num < 0:
    print("Número inválido")
    exit()
else:
    base = num - 1

    while base > 1:
        num = num * base
        base -= 1

    print(num)