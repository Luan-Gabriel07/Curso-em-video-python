r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
print ('-'*20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('-=-'*20)
    print("Os segmento podem formar um triângulo")
    if r1 == r2 == r3:
        print("O triângulo é EQUILÁTERO")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("O triângulo é ISÓSCELES")
    elif r1 != r2 != r3:
        print("O triângulo é ESCALENO")
    print ('-=-'*20)
else:
    print ("Com esses segmentos não é possível formar um triângulo")