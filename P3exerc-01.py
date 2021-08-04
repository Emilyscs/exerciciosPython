'''faça um programa que determina o mair etre N npulmeros. a conciçao de parado é 
a entrada de u valor zero'''

maior = 0
n = int(input('Informe um número:'))

while n != 0:
  if n > maior:
    maior = n
  n = int(input('Informe um npumero:'))
print('O maior número é: ', maior)