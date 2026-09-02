nome = str(input("Digite seu nome: ")).strip() #essa função strip serve para eliminar os espaços do inicio e do final da string
print("------------------------")
print ("Analisando seu nome...")
print (f"Seu nome em maiúsculo é: {nome.upper()}")
print (f"Seu nome em minúsculo é: {nome.lower()}")
separa = nome.split()
print (f"Seu primeiro nome é {nome.find(' ')} e tem {len(separa)} letras")
print (f"Seu nome tem {len(nome)-nome.count(' ')} letras") #ja essa função vai tirar os espaços estre as strings 
print ("------------------------")