"""8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.
"""

print("Olá! Vamos calcular o seu salário mensal. Informe o valor que você ganha por hora e o número de horas trabalhadas no mês.")
valor_por_hora = float(input("Informe quanto você ganha por hora: R$"))
horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))
salario_total = valor_por_hora * horas_trabalhadas
print(f"O total do seu salário no referido mês é: R${salario_total:.2f}")