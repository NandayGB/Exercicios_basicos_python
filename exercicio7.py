"""Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura)."""

print("Olá! Vamos calcular o seu Índice de Massa Corporal (IMC). Informe seu peso em kg e sua altura em metros.")

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura * altura)

print(f"\nSeu Índice de Massa Corporal (IMC) é {imc:.2f}.")