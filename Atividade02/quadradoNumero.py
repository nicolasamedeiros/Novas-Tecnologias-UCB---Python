def quadrado_por_impar(numero):
    soma_impares = 0
    numero_impar = 1

    for i in range(numero):
        soma_impares += numero_impar
        numero_impar += 2
    return soma_impares

numero = int(input("Digite um numero: "))
quadrado = quadrado_por_impar(numero)
print("O quadrado de {} é {}".format(numero, quadrado))