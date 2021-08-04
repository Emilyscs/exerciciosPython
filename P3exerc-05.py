'''
Faça um programa que leia o nome do usuário e a senha
e não aceite a senha igual ao nome do usuário, mostrando
uma mensagem de erro e voltando a pedir as informações.
'''

usuario = input('Informe o nome de usuário: ')
senha = input('Informe uma senha: ')

while usuario == senha:
  print('A senha não deve ser igual ao nome de usuário, tente novamente. ')
  usuario = input('Informe o nome de usuário: ')
  senha = input('Informe uma senha: ')