#Faça um programa que pergunte quanto você ganha por hora e o número
#de horas trabalhadas no mês. Calcule e mostre o total de seu salário no referido mês.

horas_mes = int(input("Informe a quantidade de horas trabalhadas no mês: "))
sal_hora = int(input("Informe o seu ganho por hora: "))

total_sal = horas_mes * sal_hora

print("Seu salário mensal é de {0}".format(total_sal))