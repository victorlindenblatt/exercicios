#faça um jogo de pedra papel e tesoura recendo os dados do usuário
import random


opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Escolha uma opção (pedra, papel ou tesoura): ").lower()
computador = random.choice(opcoes)

print("Você escolheu:", jogador)
print("O computador escolheu:", computador)

if jogador == computador:
    print("Empate!")
elif jogador == "pedra":
    if computador == "papel":
        print("Você perdeu!")
    else:
            print("Você ganhou!")
elif jogador == "papel":
    if computador == "tesoura":
            print("Você perdeu!")
    else:
            print("Você ganhou!")
elif jogador == "tesoura":
    if computador == "pedra":
        print("Você perdeu!")
    else:
        print("Você ganhou!")
else:
        print("Opção inválida. Por favor, escolha entre pedra, papel ou tesoura.")

