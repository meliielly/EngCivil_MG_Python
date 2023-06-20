# • Questão 3 : Implementar duas funções: a) Uma que converta temperatura em graus Celsius para Fahrenheit. b) Outra que converta temperatura em graus Fahrenheit para Celsius.

# Aluna: Melissa Gabriely GRR202321572

def celsius(f):
    c = (f-32)*5/9
    return c


def fahrenheit(c):
    f = (c*9/5)+32
    return f


op = 0

print('\nSelecione uma opção:\n')
op = int(input(
    '\n[1] Converter temperatura para Celsius\n[2] Converter temperatura para Fahrenheit\n[3] Sair\n>'))

if op == 1:
    tempF = float(input('\nDigite a temperatura em Fahrenheit: '))
    convC = celsius(tempF)
    print('\nA conversão de ', tempF, ' °F é ', convC, ' °C')

elif op == 2:
    tempC = float(input('\nDigite a temperatura em Celsius: '))
    convF = celsius(tempC)
    print('\nA conversão de ', tempC, ' °C é ', convF, ' °F')

else:
    print('\n')
