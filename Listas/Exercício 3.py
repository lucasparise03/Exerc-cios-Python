#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = [0, 0, 0, 0, 0]
x = 0
soma = 0

while x < 5:
    notas[x] = float(input(f"Nota{x}: "))
    soma += notas[x]
    x += 1
x = 0
while x < 5:
    print(f"Notas{[x]}: {notas[x]} ")
    x += 1
print(f"Média final: {soma / x}")