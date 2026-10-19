soma_num = 0
for cont in range (1,7,1):
    num = int(input(f"Digite o número {cont}°: "))
    if num % 2 == 0:
        soma_num = soma_num + num
print (f"A soma de todos os números pares é de: {soma_num}")