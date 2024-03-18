#Converte segundos em dias, horas e minutos

seg = int(input("Digite a quantidade em segundos: "))

print("{} segundos equivalem a {:.0f} dias" .format(seg, seg / 86400))
print("{} segundos equivalem a {:.0f} horas" .format(seg, seg / 3600))
print("{} segundos equivalem a {:.0f} minutos" .format(seg, seg / 60))