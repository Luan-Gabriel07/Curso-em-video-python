n = str(input("Informe seu nome completo: ")).strip()
nome = n.split() #fatiar as strings em pedaços separados por espaços
print (f"Seu primeiro nome: {nome[0]}")
print (f"Seu ultimo nome: {nome[len(nome)-1]}")