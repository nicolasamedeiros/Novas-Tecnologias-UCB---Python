frase = input("Digite uma frase: ")
contador = {}

for caractere in frase:
    if caractere.isalpha():
        if caractere in contador:
            contador[caractere] += 1
        else:
            contador[caractere] = 1

print("Dicionário de contagem de caracteres:")
print(contador)
