import random
print ('-=-'*20)
print ("Sou seu computador...")
print ("Acabei de pensar em um número entre 0 e 10")
print ("Será que você consegue adivinhar qual foi?")
print ('-=-'*20)
computador = random.randint (1,10)
tentativa = 0
tentativa_usuario = 0
while tentativa_usuario != computador:
    tentativa_usuario = int(input("Qual é o seu palpite: "))
    tentativa += 1
    print ('-'*20)
    if tentativa_usuario == computador:
        print (f"Acertou com {tentativa} tentativas. Parabéns!")
    elif tentativa_usuario > computador:
        print ("Menos... Tente mais uma vez.")
    else:
        print ("Mais... Tente mais uma vez.")
      