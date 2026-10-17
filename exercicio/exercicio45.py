
import random

print("=== PEDRA, PAPEL E TESOURA ===")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

jogador = int(input("Escolha sua jogada: "))

computador = random.randint(1, 3)

if jogador == 1:
    print("Você escolheu Pedra")
elif jogador == 2:
    print("Você escolheu Papel")
elif jogador == 3:
    print("Você escolheu Tesoura")
else:
    print("Opção inválida!")

if jogador >= 1 and jogador <= 3:
    if computador == 1:
        print("Computador escolheu Pedra")
    elif computador == 2:
        print("Computador escolheu Papel")
    else:
        print("Computador escolheu Tesoura")

    if jogador == computador:
        print("Empate!")
    elif jogador == 1 and computador == 3:
        print("Você venceu!")
    elif jogador == 2 and computador == 1:
        print("Você venceu!")
    elif jogador == 3 and computador == 2:
        print("Você venceu!")
    else:
        print("Você perdeu!")
