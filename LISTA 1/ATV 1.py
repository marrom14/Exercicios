quantidade_litros = int(input("Informe a Quantidade de Litros: "))
tipo_combustivel = input("(A)lcool ou (G)asolina:" )
if tipo_combustivel.strip().upper() == "A":
    print("Como você comprou", quantidade_litros, "Litros de ÁLCOOL")
    if quantidade_litros < 20:
        total = quantidade_litros * 2.90 * 0.97
    else:
        total = quantidade_litros * 2.90 * 0.95
else:
    print("Como você comprou", quantidade_litros, "Litros de GASOLINA")
    if quantidade_litros < 20:
        total = quantidade_litros * 3.30 * 0.96
    else:
        total = quantidade_litros * 3.30 * 0.94
print("O total é: " "R$" '{:.2f}'.format(total))