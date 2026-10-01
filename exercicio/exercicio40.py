not1 = float(input("Nota primeiro ciclo: "))
not2 = float(input("Nota segundo ciclo: "))
# not3 = float(input("Nota terceiro ciclo: "))
media = (not1 + not2) / 2
print (f"A média do aluno {media:.2f}")
if media >= 7:
    print ("Aluno APROVADO")
elif media < 5:
    print ("Aluno REPROVADO")
elif media >= 5 and media < 7:
    print ("Aluno em RECUPERAÇÃO")