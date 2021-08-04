'''
Faça um gerador de tabuada de 1 a 10. O usuário deve
informar um número e a saída deve ser conforme o exemplo abaixo: 

Tabuada de 2: 
2 x 0 = 0
2 x 1 = 2
...
2 x 10 = 20
'''

num = int(input('Informe um número de 1 a 10: '))

while num < 1 or num > 10:
  print('Número inválido, tente novamente.')
  num = int(input('Informe um número de 1 a 10: '))

print('Tabuada de {0}:'.format(num))
for n in range(0, 11):
  print('{0} x {1} = {2}'.format(num, n, (num * n)))
