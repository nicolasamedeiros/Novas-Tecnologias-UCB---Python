#Espaçamento entre números

numeros = input("Digite 5 numeros: ")

if len(numeros) == 5 :
    numerosEspaco = " ".join(numeros)
    print("Números com espaçamento: ",  " ".join(numeros))
else :
    print("Digite 5 números")
