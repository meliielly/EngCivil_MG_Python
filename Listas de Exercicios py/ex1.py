# Questão 1 : Através do Teorema de Pitagoras estime o tamanho da hipotenusa a partir da entrada no teclado dos valores do cateto oposto e adjacente. Apresente o algoritmo e a solução.

#Aluna: Melissa Gabriely GRR202321572

import math

co = 0
ca = 0

print('Forneça os valores dos catetos para o cálculo da Hipotenusa:\n')
co = int(input('\nInforme o valor do cateto oposto:\n>'))
ca = int(input('\nInforme o valor do cateto adjacente:\n>'))

hip = (co*co) + (ca*ca)
result = math.sqrt(hip)

print("\nHipotenusa: ", result)
print("Hipotenusa Arredondada: ", round(result))