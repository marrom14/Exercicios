quantidade_morangos = int(input("Quantidade em Kg de morangos comprados:"))
quantidade_macas = int(input("Quantidade em Kg de maçãs compradas:"))
if quantidade_morangos > 5:
    total_morangos = quantidade_morangos * 2.20
else:
    total_morangos = quantidade_morangos * 2.50
if quantidade_macas> 5:
    total_macas = quantidade_macas * 1.50
else:
    total_macas = quantidade_macas * 1.80
TOTAL_FRUTAS = total_morangos + total_macas
if TOTAL_FRUTAS > 25 or (total_morangos + total_macas) > 8:
    TOTAL_COMPRAS = TOTAL_FRUTAS * 0.90
else:
    TOTAL_COMPRAS = TOTAL_FRUTAS
print("O valor total da compra a ser pago é de:" "R$" '{:.2f}'.format(TOTAL_COMPRAS))