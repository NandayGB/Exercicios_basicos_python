"""
5.Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.

"""

##5.

print("Olá! Vamos calcular o seu salário líquido com base no imposto de renda.")

salario_bruto = float(input("Informe o valor do salário bruto: R$"))

if salario_bruto <= 1903.98:
    desconto_ir = 0
elif salario_bruto <= 2826.65:
    desconto_ir = salario_bruto * 0.075
elif salario_bruto <= 3751.05:
    desconto_ir = salario_bruto * 0.15
elif salario_bruto <= 4664.68:
    desconto_ir = salario_bruto * 0.225
else:
    desconto_ir = salario_bruto * 0.275


salario_liquido = salario_bruto - desconto_ir

print(f"O salário líquido após o desconto do Imposto de Renda é: R${salario_liquido:.2f}")
