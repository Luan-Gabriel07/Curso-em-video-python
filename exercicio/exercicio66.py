n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input("Digite um valor (999 para parar): "))
    if n == 999:
        break
    else:
        cont += 1
        soma += n
print (f"A soma dos {cont} valores foi {soma}!")