def calcular_verificador(num_conta):
    soma_digitos = 0
    for digito in str(num_conta):
        soma_digitos += int(digito)

    resto_divisao = soma_digitos % 10

    if resto_divisao != 0:
        digito_verificador = 10 - resto_divisao
    else:
        digito_verificador = 0
    return digito_verificador

def adicionar_digito_verificador(num_conta):
    digito_verificador = calcular_verificador(num_conta)
    num_conta_com_digito = "00{}-{}".format(num_conta, digito_verificador)
    return num_conta_com_digito

num_conta = 7314
num_conta_com_digito = adicionar_digito_verificador(num_conta)
print("O número da conta com o dígito verificador é: {}".format(num_conta_com_digito))