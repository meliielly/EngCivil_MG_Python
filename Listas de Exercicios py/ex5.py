# • Questão 5 : Sabendo que a velocidade da onda de gravidade em águas profundas dependem da profundidade do mar h, e da aceleração da gravidade g, de acordo com a equação abaixo. Crie uma função (def) que calcule a velocidade da onda de acordo com valores h de entrada.

# Aluna: Melissa Gabriely GRR203232172

import math


def velocidadeOnda(h):
    v = math.sqrt(10*h)
    return v


alt = float(input('\nDigite o valor da altura: \n>'))
velocidade = velocidadeOnda(alt)
print('\nA velocidade da onda é: ', velocidade)
print('\nVelocidade da onda Arredondada: ', round(velocidade))
