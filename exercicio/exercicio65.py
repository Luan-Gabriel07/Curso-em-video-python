cont = 0
soma = 0
opc = 's'
while opc in 'Ss':
    num = float(input("Digite um número: "))
    opc = str(input("Quer continuar [S/N]: ")).upper().strip()[0]
    cont +=1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print (f"Você digitou {cont} númeoros e a média foi de {soma/cont:.2f}")
print (f"O maior valor foi {maior:.0f} e o menor foi {menor:.0f}")
