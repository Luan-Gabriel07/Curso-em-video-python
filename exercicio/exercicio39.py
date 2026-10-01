nascimento = int(input("Ano de nascimento: "))
idade = 2026 - nascimento
print (f"Quem nasceu em {nascimento} tem {idade} anos em 2026")
if idade == 18:
    print ("Você tem que se alistar no exercito com URGÊNCIA")
elif idade > 18:
    exedeu_idade = idade - 18
    print (f"Você ja deveria ter se alistado há {exedeu_idade} anos")
    exedeu_ano = 2026 - exedeu_idade
    print (f"Seu alistamento foi em {exedeu_ano}")
elif idade < 18:
    falta_idade = 18 - idade
    print (f"Ainda falta {falta_idade} anos para o alistamento")
    ano_alistamento = 2026 + falta_idade
    print (f"Seu alistamento será em {ano_alistamento}")