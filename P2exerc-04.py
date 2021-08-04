'''
Tendo como dados de entrada a altura e o sexo de uma pessoa. Construa um programa que calcule seu peso ideal, utilizando as segints fórmulas:
Para homens: (72.7*altura) - 58
para mulheres: (62.1*altura) - 44.7
'''

altura = float(input('Informe sua altura: '))
sexo = input('Informe o sexo f/m: ')

if sexo.lower() == 'f':
    peso_ideal = (62.1*altura) - 44.7
if sexo.lower() == 'm':
    peso_ideal = (72.7*altura) - 58
else:
    print('Sexo não reconhecido, tente novamente.')

print('Seu peso ideal é: {0}'.format(peso_ideal))