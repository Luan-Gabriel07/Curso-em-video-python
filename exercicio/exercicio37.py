num = int(input("Digite um número inteiro: "))
print("")
print("Para qual base numerica você quer transfomar?")
print ("[1] Binário")
print ("[2] Octal")
print ("[3] Hexadecimal")
opc = int(input("Escolha a base: "))
if opc == 1:
    print (f"{num} convertido para binário é igual a {bin(num) [2:]}")
elif opc == 2:
    print (f"{num} convertido para octal é igual a {oct(num)[2:]}")
elif opc == 3:
    print (f"{num} convertido para hexadecimal é igual a {hex(num)[2:]}")
else:
    print ("Opção inválida!")