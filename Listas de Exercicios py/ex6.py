# • Questão 6 : Utilizando a função construído no exercício anterior, crie um laço/loop para calcular a velocidade da onda automaticamente variando de 1 a 10 m de profundidade.

# Aluna: Melissa Gabriely GRR20232172

import math


def velocidadeOnda(h):
    v = math.sqrt(10*h)
    return v


for i in range(11):
    velocidade = velocidadeOnda(i)
    print('\nCom a altura de [', i,
          'm ] a velocidade da onda é: ', velocidade)
    print('\nVelocidade da onda Arredondada: ', round(velocidade))
