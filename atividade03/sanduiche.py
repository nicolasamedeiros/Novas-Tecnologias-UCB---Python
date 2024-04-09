sandwich_orders = ["Atum", "Frango", "Vegetariano", "Bacon"]
finished_sandwiches = []

# Preparando os sanduíches
while sandwich_orders:
    pedido = sandwich_orders.pop(0)
    print("Preparei seu sanduíche de", pedido)
    finished_sandwiches.append(pedido)

# Exibindo os sanduíches prontos
print("\nSanduíches prontos:")
for sanduiche in finished_sandwiches:
    print(sanduiche)
