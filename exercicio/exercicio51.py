print ('='*20)
print ("10 TERMOS DE UMA PA")
print ('='*20)
ptermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = ptermo + (11 - 1) * razao
for cont in range(ptermo,decimo,razao):
    print (cont, end= ' -> ')
print ("ACABOU")