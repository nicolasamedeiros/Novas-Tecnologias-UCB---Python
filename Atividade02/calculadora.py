ope = 1

while ope!=0:
    num1 = int(input("Entre com um número: "))
    num2 = int(input("Entre com outro numero: "))
    ope = int(input("Digite a operação desejada: \n \
    1- Soma\n \
    2- Subtração\n \
    3- Multiplicação\n \
    4 - Divisão \n \
    0 - Para sair \n"))
    if ope==1:
        print(f"A soma de {num1}+{num2}={num1+num2} \n")
    elif ope==2:
        print(f"A subtração de {num1}-{num2}={num1-num2} \n")
    elif ope==3:
        print(f"A multiplicação de {num1}x{num2}={num1*num2} \n")
    elif ope==4:
        print(f"A divisão de {num1}/{num2}={num1/num2} \n")
    else:
        print("Opção inválida")
