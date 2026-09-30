import random 
import time
num = random.randint(0, 5)
print ("-=-" *20)
print ("Vou pensar em um número de 0 a 5. Tente adivinhar...")
print ("-=-" *20)
escolha = int(input("Em que número eu pensei? "))
print ("Processando...")
time.sleep(1)
if escolha == num:
    print ("Parabéns! Você conseguiu me vencer!")
else:
    print (f"Ganhei! Eu pensei no numero {num} e não no numero {escolha}")