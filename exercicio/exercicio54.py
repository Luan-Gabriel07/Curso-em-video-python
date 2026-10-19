from datetime import date
atual = date.today().year
maior_idade = 0
menor_idade = 0
for cont in range (1,8,1):
    ano = int(input(f"Em que ano a {cont}° nasceu? "))
    if atual - ano >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print (f"Ao todo tivemos {maior_idade} pessoas maiores de idade")
print (f"E também tivemos {menor_idade} pessoas menores de idade")

    