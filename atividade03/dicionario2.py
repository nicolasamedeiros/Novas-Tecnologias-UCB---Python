usuario = {"first_name":"Nicolas", "Last name":"Medeiros", "age":20, "city":"Brasília"}
usuario2 = {"first_name":"Junior", "Last name":"Linz", "age":17, "city":"São Paulo"}
usuario3 = {"first_name":"João", "Last name":"Silva", "age":25, "city":"Rio de Janeiro"}

people = [usuario, usuario2, usuario3]

for usuario in people:
    print(usuario["first_name"])
    print(usuario["Last name"])
    print(usuario["age"])
    print(usuario["city"])
    print()