def fibonacci(num):
    if num <= 0:
        return("O número deve ser maior ou igual a 1")
    elif num == 1 or num == 2:
        return 1
    else:
        a = 1 
        b = 1
        for i in range(2, num):
            a, b = b, a + b
        return b 
    
num = 7
termo = fibonacci(num)
print("O {}-ésimo terma da sequência de Fibonacci é: {}".format(num, termo))