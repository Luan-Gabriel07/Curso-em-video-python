import math
num = int(input("Digite um número para calcular o seu fatorial: "))
f = math.factorial(num)
cont = num
while cont > 0:
    print (cont, end= ' x')
    print (' x ' if cont > 1 else ' = ', end='')
    cont -= 1
print (f)
