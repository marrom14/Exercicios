# Leia a idade, altura e o peso de 3 pessoas. calcule e mostre:
# a) a quantidade de pessoas com a idade superior a 20 anos;
# b) a média das alturas das pessoas com idade entre 15 e 18 anos;
# c) a porcentagem de pessoas com peso inferior a 60 quilos entre todas as pessoas analisadas.

IDADE_1 = int(input("Informe a idade da primeira pessoa: "))
ALTURA_1 = float(input("Informe a altura da primeira pessoa: "))
PESO_1 = float(input("Informe o peso da primeira pessoa: "))

IDADE_2 = int(input("Informe a idade da segunda pessoa: "))
ALTURA_2 = float(input("Informe a altura da segunda pessoa: "))
PESO_2 = float(input("Informe o peso da segunda pessoa: "))

IDADE_3 = int(input("Informe a idade da terceira pessoa: "))
ALTURA_3 = float(input("Informe a altura da terceira pessoa: "))
PESO_3 = float(input("Informe o peso da terceira pessoa: "))

if IDADE_1 > 20:
    I1 = 1
else:
    I1 = 0
if IDADE_2 > 20:
    I2 = 1
else:
    I2 = 0
if IDADE_3 > 20:
    I3 = 1
else:
    I3 = 0
total_idades = I1 + I2 + I3
print("Das pessoas informadas", total_idades, "tem idade superior a 20 anos!")

print("Agora vamos calcular a média das alturas!!!")
if IDADE_1 >= 15 and IDADE_1 <= 18:
    H1 = ALTURA_1
else:
    None
if IDADE_2 >= 15 and IDADE_2 <= 18:
    H2 = ALTURA_2
else:
    None
if IDADE_3 >= 15 and IDADE_3 <= 18:
    H3 = ALTURA_1
else:
    None
total_alturas = (H1 + H2 + H3) / (H1 +H2 + H3)
print("A média das alturas das pessoas informadas é: ", total_alturas, "!!")
















