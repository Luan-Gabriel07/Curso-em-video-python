print ("GERADOR DE PA")
print ('-=-'*20)
termo1 = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
cont = 1
while cont < 10:
    print (termo1, end=' -> ')
    termo1 +=razao
    cont +=1
print ("FIM")