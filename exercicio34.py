salario = float(input("Qual o salário do funcionario? "))
if salario > 1250:
    aumento = salario * 0.10
    salario_atu = salario + aumento
else :
    aumento = salario * 0.15
    salario_atu = salario + aumento
print (f"O funcionario tem um salário de {salario} e com o aumento ele recebe {salario_atu}")