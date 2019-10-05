codigo_usuario = int(input("Digite o código:"))
if codigo_usuario != 1234:
    print("Usuário inválido!!!")
else:
    senha = int(input("Digite a senha:"))
    if senha != 9999:
        print("Senha Inválida!!!")
    else:
        print("ACESSO PERMITIDO!!!")