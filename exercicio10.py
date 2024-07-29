"""10. Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área."""

print("Vamos criar uma mensagem amigável usando quatro variáveis. Informe seu nome, curso, universidade e ano de ingresso.")

nome_estudante = input("Qual é o seu nome? ")
curso = input("Qual é o seu curso? ")
universidade = input("Qual é a sua universidade? ")
ano_ingresso = input("Em qual ano você ingressou no curso? ")

print(f"\nOlá {nome_estudante}, é um prazer te conhecer!")
print(f"Você está cursando {curso} na {universidade}.")
print(f"Você começou em {ano_ingresso}, que legal!")
print(f"Espero que sua jornada acadêmica esteja sendo incrível. Vamos fazer o melhor dela!")