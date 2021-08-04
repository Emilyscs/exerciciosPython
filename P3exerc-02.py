'''
faça um programa que conte de 1 a 100 e a casa múltiplo de 10 emita uma mensagem: 'Multiplo de 100"
'''
n = 0
for n in range(1, 101):
  print(n)
  if n % 10 == 0:
    print('Múltiplo de 10')