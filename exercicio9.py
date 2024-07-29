""" 9.Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.
"""

print("Vamos calcular o total de calorias queimadas em um mês com base no seu número de horas de exercício físico por semana.")


horas_por_semana = float(input("Quantas horas você faz de exercício físico por semana? "))

calorias_por_minuto = 5

minutos_por_semana = horas_por_semana * 60

calorias_por_semana = minutos_por_semana * calorias_por_minuto

calorias_por_mes = calorias_por_semana * 4

print(f"\nVocê queima aproximadamente {calorias_por_mes:.2f} calorias em um mês.")