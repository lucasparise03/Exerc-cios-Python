"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. """

login = input("Informe seu login: ")
senha = input("Informe sua senha: ")

while login == senha:
    login = input("Login e senha não podem ser iguais, altere seu login aqui: ")
    login = input("Informe seu novo login: ")
    senha = input(("Informe sua senha: "))