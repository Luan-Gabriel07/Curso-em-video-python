sexo = str(input("Informe seu sexo [M/F]: ")).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()
if sexo == 'M' or sexo == 'm':
    print ("Sexo M registrado com sucesso!")
else:
    print ("Sexo F registrado com sucesso!")