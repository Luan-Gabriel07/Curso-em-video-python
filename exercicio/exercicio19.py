import random
lista = []
p = input("Primeiro aluno: ")
lista.append(p)
s = input("Segundo aluno: ")
lista.append(s)
t = input("Terceiro aluno: ")
lista.append(t)
q = input("Quarto aluno: ")
lista.append(q)
qu = input("Quinto aluno: ")
lista.append(qu)
sorteio = random.choice(lista)
print (sorteio)