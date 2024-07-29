## 3 .Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.

print("Olá! Informe a quantidade de quilômetros que deseja converter para metros, centímetros e milímetros:")

# Solicita ao usuário a quantidade de quilômetros
quilometros = float(input("Informe a quantidade de quilômetros: "))

# Converte a quantidade de quilômetros para metros, centímetros e milímetros
metros = quilometros * 1000
centimetros = quilometros * 100000
milimetros = quilometros * 1000000

# Exibe os resultados
print(f"{quilometros} quilômetros são equivalentes a:")
print(f"- {metros} metros")
print(f"- {centimetros} centímetros")
print(f"- {milimetros} milímetros")


