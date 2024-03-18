#Exibe a soma, subtração, multiplicação, divisão e potência de dois números

import math

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = math.pow(n1, n2)

print("A soma dos números é: ", soma)
print("A subtração dos números é: ", subtracao)
print("A multiplicação dos números é: ", multiplicacao)
print("A divisão dos números é: ", divisao)
print("A potência dos números é: ", potencia)
