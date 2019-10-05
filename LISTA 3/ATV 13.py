produto = float(input("Digite o valor do produto: "))
if produto < 20:
    lucro_45 = produto + produto * 0.45
    print("O valor de revenda é: " "R$ " '{:.2f}'.format(lucro_45))
else:
    produto > 20
    lucro_30 = produto + produto * 0.30
    print("O valor de revenda é: " "R$ " '{:.2f}'.format(lucro_30))