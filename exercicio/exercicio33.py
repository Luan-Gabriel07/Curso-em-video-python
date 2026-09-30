valo1 = int(input("Primeiro valor: "))
valo2 = int(input("Sugundo valor: "))
valo3 = int(input("Terceiro valor: "))
menor = valo1
if valo2 < valo1 and valo2 < valo3:
    menor = valo2
if valo3 < valo1 and valo3 < valo2:
    menor = valo3
print (f"O menor valor é igual a {menor}")

maior = valo1
if valo2 > valo1 and valo2 > valo3:
    maior = valo2
if valo3 > valo1 and valo3 > valo2:
    maior = valo3
print (f"O maior valor é igual a {maior}")
