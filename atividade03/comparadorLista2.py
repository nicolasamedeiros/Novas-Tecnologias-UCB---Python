versao_inicial = [1, 2, 3, 4, 5]
versao_alterada = [2, 3, 5, 6, 7]

# Convertendo as listas em conjuntos
inicial = set(versao_inicial)
alterada = set(versao_alterada)

# Elementos que não mudaram
nao_mudaram = inicial.intersection(alterada)
print("Elementos que não mudaram:", nao_mudaram)

# Novos elementos
novos_elementos = alterada.difference(inicial)
print("Novos elementos:", novos_elementos)

# Elementos removidos
removidos = inicial.difference(alterada)
print("Elementos que foram removidos:", removidos)
