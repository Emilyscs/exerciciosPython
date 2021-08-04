'''
cosntrua um programa que leia 10 valores inteiros e positivos e\;
a) encontre o maior valor 
b) encontre o menor valor
c) calcule a média dos números lidos
'''
maior = -9999
menor = 9999
soma = 0

for i in range(1, 11):
  num = int(input('Informe um número: '))
  if num > 0:
    if num > maior:
      maior = num
    if num < menor:
      menor = num
    soma = soma + num
  else:
    num = int(input('Número invalido, insira novamente: '))
media = soma / 10

print('O maior número é ', maior)
print('O menor número é ', menor)
print('A media dos números é ', media)