# • Questão 7 : Crie um algoritmo para o jogo do adivinhe o número. Ou seja, o computador escolhe um número aleatório de 0 a 100 e você deve acertar baseado nas dicas de que seu chute foi um valor acima ou abaixo do número escolhido pelo computador

# Aluna: Melissa Gabriely GRR20232172

from random import randint

print("JOGO ADIVINHE O NÚMERO!")
sorteado = randint(1, 100)
chute = 0

while chute != sorteado:
    chute = int(input("\nChute um numero de 1 a 100:\n>"))
    if chute == sorteado:
        print("Vc venceu!!!  O numero sorteado era: {0} ".format(chute))
    else:
        if chute > sorteado:
            print("\nChute um valor menor!")
        else:
            print("\nChute um valor maior!")
