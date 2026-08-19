import math
cat_op = float(input("Comprimento do cateto oposto: "))
cat_ad = float(input("Comprimento do cateto adjacente: "))
hipo = math.pow(cat_op,2) + math.pow(cat_ad,2)
print (f"A hipotenusa vai medir {math.sqrt(hipo):.2f}")

# calculo da hipotenusa
#h² = cat op² + cat ad²