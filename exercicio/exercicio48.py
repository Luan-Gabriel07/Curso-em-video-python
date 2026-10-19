div_tres = 0
soma_cont = 0
for cont in range (1,501,2):
    if cont % 3 == 0:
        div_tres = div_tres + 1
        soma_cont = soma_cont + cont
print (f"Soma de todos os {div_tres} valores é igual a {soma_cont}")