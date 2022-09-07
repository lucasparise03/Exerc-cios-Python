"""Criar um Menu com:
nome maior que 3 caracteres
idade entre 0 e 150 anos
salario maior que zero
sexo F ou M
estado civil S C V D
"""

nome = input("Informe seu nome: ")

while len(nome) <= 3:
    nome = input("Seu nome deve ter mais de 3 caracteres"
                 "New name: ")

idade = int(input("Informe sua idade: "))

while (idade < 0) or (idade > 151):
    idade = int(input("Informe uma idade entre 0 e 150."
                      "Idade nova: "))

salario = float(input("Informe seu salário: "))

while salario <= 0:
    salario = float(input(("Informe um salário válido: ")))

sexo = input("Informe seu sexo: ")

while (sexo != 'f') and (sexo != 'm'):
    sexo = input("Para de frescura cara, é F ou M")

estado = input("Informe seu estado de relacionamento: ")

while(estado != 'S') and (estado != 'C') and (estado != 'V') and (estado != 'D'):
    estado = input("Estado inválido, estado correto: ")