lista = [12, -12, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

#Imprimir o maior elemento
maior_elemento = max(lista)
print("Maior elemento:", maior_elemento)

#Imprimir o menor elemento
menor_elemento = min(lista)
print("Menor elemento:", menor_elemento)

#Imprimir os números pares
numeros_pares = [num for num in lista if num % 2 == 0]
print("Números pares:", numeros_pares)

#Imprimir o número de ocorrências do primeiro elemento da lista
primeiro_elemento = lista[0]
num_ocorrencias = lista.count(primeiro_elemento)
print("Número de ocorrências do primeiro elemento:", num_ocorrencias)

#Imprimir a média dos elementos
soma = sum(lista)
media = soma / len(lista)
print("Média dos elementos:", media)

#Imprimir a soma dos elementos de valor negativo
soma_negativos = sum(num for num in lista if num < 0)
print("Soma dos elementos de valor negativo:", soma_negativos)
