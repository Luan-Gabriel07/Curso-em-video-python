valor = 0
cont = 0
soma = 0
while valor != 999:
    valor = int(input("Digite um número [999 para parar]: "))
    if valor == 999:
        cont += 0
        soma +=0
    else:
        cont += 1
        soma += valor
print (f"Você digitou {cont} valores e soma entre eles foi {soma}")
