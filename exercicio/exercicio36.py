valor_casa = float(input("Qual o valor da casa: R$ "))
salario = float(input("Salário do comprador: "))
anos = int(input("Quantos anos de financiamento? "))
meses = anos * 12
prestacao_mensal = valor_casa / meses
minimo = salario * 0.3
print('-=-'*20)
print(f"A sua prestação é de {prestacao_mensal:.2f}")
print (f"Você pode pagar parcelas de até {minimo:.2f}")
if prestacao_mensal <= minimo:
    print ("Empréstimo APROVADO")
else: 
    print ("Empréstimo REPROVADO")
print('-=-'*20)