# Questão 2 : Refaça a questão 1, entretanto, utilizando o comando def para criar uma função para calcular a hipotenusa.

#Aluna: Melissa Gabriely GRR202321572

import math

def hipotenusa(catetoOposto,catetoAdjacente):

    hip = (catetoOposto*catetoOposto) + (catetoAdjacente*catetoAdjacente)
    result = math.sqrt(hip)
    return result
   
print('Forneça os valores dos catetos para o cálculo da Hipotenusa:\n')
co = int(input('\nInforme o valor do cateto oposto:\n>'))
ca = int(input('\nInforme o valor do cateto adjacente:\n>'))

hip = hipotenusa(co, ca)

print("\nHipotenusa: ", hip)
print("Hipotenusa Arredondada: ", round(hip))