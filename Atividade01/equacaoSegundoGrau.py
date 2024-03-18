#equação de segundo grau

import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = math.pow(b,2) - (4*a*c)

if delta < 0:
    print("A equação não possui raízes reais")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("As raízes da equação são {} e {}" .format(x1, x2))