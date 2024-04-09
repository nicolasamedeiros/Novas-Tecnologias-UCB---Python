lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

# Valores comuns nas duas listas
comuns = conjunto1.intersection(conjunto2)
print("Valores comuns às duas listas:", comuns)

# Valores que só existem na primeira lista
somente_na_primeira = conjunto1.difference(conjunto2)
print("Valores que só existem na primeira lista:", somente_na_primeira)

# Valores que existem na segunda lista
somente_na_segunda = conjunto2.difference(conjunto1)
print("Valores que só existem na segunda lista:", somente_na_segunda)

# Lista com os elementos não repetidos das duas listas
nao_repetidos = list(conjunto1.union(conjunto2))
print("Lista com os elementos não repetidos das duas listas:", nao_repetidos)

# A primeira lista sem os elementos repetidos na segunda
sem_repetidos_na_segunda = list(conjunto1.difference(comuns))
print("A primeira lista sem os elementos repetidos na segunda:", sem_repetidos_na_segunda)
