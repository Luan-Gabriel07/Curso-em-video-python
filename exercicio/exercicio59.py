import time
opc = 0
num1 = float(input("Primeiro valor: "))
num2 = float(input("Segundo valor: "))
while opc != 5:
    print("[1] SOMAR")
    print("[2] MULTIPLICADOR")
    print("[3] MAIOR")
    print("[4] NOVOS NÚMEROS")
    print("[5] SAIR DO PROGRAMA")
    opc = int(input(">>>>>> QUAL É A SUA OPÇÃO? "))
    if opc == 1:
        print (f"A soma entre {num1:.0f} + {num2:.0f} = {num1 + num2:.0f}")
    elif opc == 2:
        print (f"A multiplicação entre {num1:.0f} x {num2:.0f} = {num1 * num2:.0f}")
    elif opc == 3:
        maior_num = num1
        if num2 > maior_num:
            print (f"O maior número é o {num2:.0f}")
        else:
            print(f"O maior número é o {maior_num:.0f}")
    elif opc == 4:
        num1 = float(input("Primeiro valor: "))
        num2 = float(input("Segundo valor: "))
    elif opc == 5:
        print ("Saindo...")
    else:
        print ("Opção inválida")
    print('-==-'*20)
    time.sleep(0.5)