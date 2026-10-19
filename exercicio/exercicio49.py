import time
num = int(input("Digite um número para ver sua tabuada: "))
for cont in range (1,11,1):
    print (f"{num} x {cont} = {num * cont}")
    time.sleep(0.5)
    