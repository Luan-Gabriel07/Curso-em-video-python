import time
velocidade = float(input("Informe a velocidade do carro: "))
print ('-=-'*20)
print ("Processando...")
print ('-=-'*20)
time.sleep(2)
if velocidade > 80:
    velo_acima = velocidade - 80
    multa = velo_acima * 7
    print ("MULTADO! Você excedeu o limite permitido que é de 80km/h")
    print (f"Você deve pagar uma multa de R${multa:.2f}!")
    print ("Tenha um bom dia! Dirija com segurança!")
else:
    print ("Tenha um bom dia! Dirija com segurança!")