print ("GERADOR DE PA")
print ('-=-'*20)
termo1 = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
cont = 1
quantidade_termos = 10
total = 0
while quantidade_termos != 0:
    total += quantidade_termos
    while cont <= total:
        print (termo1, end=' -> ')
        termo1 +=razao
        cont +=1
    print ("PAUSA")
    quantidade_termos = int(input("Quantos termos você quer mostrar  a mais? "))
print (f"Progressão finalizada com {total} termos mostrados")