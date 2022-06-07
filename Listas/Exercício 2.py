#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = [1, 2, 15, 45, 789, 7987, 78978, 789789, 7897897, 98798789]
x = 0

while x < len(vetor):
    newlist = list(reversed(vetor)) #inverte os valores da lista.
    print({newlist[x]}) #[x] imprime o número que está no índice e soma +1, para printar o próximo.
    x += 1
