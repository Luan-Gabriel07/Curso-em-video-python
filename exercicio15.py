dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
#custo dia = 60 reias 
#0.15 reais  cada Km
custo = (dias * 60) + (km * 0.15)
print (f"O total a pagar é de R${custo:.2f}")