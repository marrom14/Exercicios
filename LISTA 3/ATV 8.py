senha = str(input("Por favor, digite a senha: "))
senha.format(int)
acesso = ("batatafrita")
if senha.strip().upper() == "BATATAFRITA":
    print("Acesso permitido!!!")
else:
    print("Você não tem acesso ao sistema!!!")