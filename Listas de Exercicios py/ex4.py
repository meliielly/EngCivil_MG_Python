# • Questão 4 : Implementar uma função que retorne verdadeiro se o número for ímpar (falso caso contrário). Testar com números de 1 a 100 através de chamada no teclado.

# Aluna: Melissa Gabriely GRR20232172

def imparOuPar(n):
    num = n/2
    return num
num = int(input('\nDigite um número: \n>'))
imparOuPar(num)

if (num%2) == 0:
    print('\nO número é PAR!')
else:
    print('\nO número é ÍMPAR!')