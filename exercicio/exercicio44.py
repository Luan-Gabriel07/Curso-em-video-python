print ("============ DISTRIBUIDORA ROCHA ============")
preco = float(input("Preço das compras: R$"))
print ("FORMAS DE PAGAMENTO:")
print ("[1] à vista dinheiro / cheque")
print ("[2] à vista cartão")
print ("[3] 2x no cartão")
print ("[4] 3x ou mais no cartão")
opc = int(input("Qual é a opção: "))
match opc:
    case 1: 
        desconto = preco * 0.10
        valor_total = preco - desconto
        print ('-=-'*20)
        print ("O valor à vista tem um desconto de 10%")
        print (f"Desconto: R${desconto:.2f}")
        print (f"Valor total: R${valor_total:.2f}")
        print ('-=-'*20)
    case 2:
        desconto = preco * 0.05
        valor_total = preco - desconto
        print ('-=-'*20)
        print ("O valor à vista tem um desconto de 5%")
        print (f"Desconto: R${desconto:.2f}")
        print (f"Valor total: R${valor_total:.2f}")
        print ('-=-'*20)
    case 3:
        valor_total = preco
        print ('-=-'*20)
        print ("O valor dividido em até 2x no cartão tem o preço normal")
        print (f"Valor total: R${valor_total:.2f}")
        print ('-=-'*20)
    case 4: 
        parcelas = int(input("Quantas parcelas? "))
        juros = preco * 0.20
        valor_total = preco + juros
        valor_parcela = valor_total / parcelas
        print ('-=-'*20)
        print (f"O valor dividido em {parcelas}x no cartão tem um juros de 20%")
        print (f"Juros: R${juros:.2f}")
        print (f"Valor da parcela: {valor_parcela:.2f}")
        print (f"Valor total: R${valor_total:.2f}")
        print ('-=-'*20)
    case _:
        print ("Opção inválida")
