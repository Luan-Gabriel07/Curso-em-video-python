divisivel = 0
num = int(input("Digite um número: "))
for cont in range(1,11,1):
    print (cont, end= ' ')
    if num % cont == 0:
        divisivel = divisivel + 1
print (f"\nO número {num} foi divisível {divisivel} vezes")
if divisivel == 2:
    print ("E por isso ele É PRIMO")
else:
    print ("E por isso ele NÃO É PRIMO")