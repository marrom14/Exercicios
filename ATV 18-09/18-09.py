idade = int(input("Informe a idade do nadador: "))
if idade == 5 or idade == 6 or idade == 7:
    idade = "pertence a categoria Infantil A!"
else:
    if idade >= 12 and idade <= 13:
        idade = "pertence a categoria Juvenil A!"
    else:
        if idade > 18:
            idade = "pertence a categoria Adulto!"
        else:
            idade = "Não pode competir!!!"
print("Este nadador", idade)


