maior_idade = 0
feminino = 0
soma_idade = 0
for cont in range (1,5):
    print (f"----- {cont}º PESSOA -----")
    nome = input("Nome: ")
    idade = int(input("Idade:"))
    sexo = input("Sexo [M/F]: ")
    soma_idade = soma_idade + idade
    if idade > maior_idade:
        maior_idade = idade
        nome_maior_idade = nome
    if sexo == 'F' or sexo == 'f' and idade < 20:
        feminino += 1
media_idade = soma_idade / 4
print ('-=-'*20)
print (f"A média de idade do grupo é de {media_idade:.1f}")
print(f"O homem mais velho tem {maior_idade} e se chama {nome_maior_idade}")
print(f"Ao todo são {feminino} mulheres com menos de 20 anos")
print ('-=-'*20)