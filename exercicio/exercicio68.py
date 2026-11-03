import random
vitoria = 0
pi = ' '
while True:
    print ("-=-"*30)
    print ("VAMOS JOGAR PAR OU ÍMPAR")
    print ("-=-"*30)
    valor = int(input("Diga um valor: "))
    while pi not in 'PI':
        pi = str(input("Par ou Ímpar? [P/I] ")).upper().strip()[0]    
        print ('-'*30)
        computador = random.randint (0,10)
        soma = computador + valor
        print (f"Você jogou {valor} e o computador {computador}. Total de {soma}")
    if pi == 'P':
        if soma % 2 == 0:
            print ("Você VENCEU!")
            vitoria += 1
        else:
            print ("Você PERDEU!")
            break
    elif pi == 'I':
        if soma % 2 == 1:
            print ("Você VENCEU!")
            vitoria += 1
        else:
            print ("Você PERDEU!")
            break
        print ("Vamos jogar novamente...")
print ('-'*30)
print (f"GAME OVER! Você venceu {vitoria} vezes")
print ('-'*30)
