'''
elabore um programa que escreva os números ímpares
dos números entre 100 e 200.
'''
contador = 0

print('Os números ímpares entre 100 e 200 são: ')
for contador in range(100, 201):
  if contador % 2 == 1:
    print(contador)