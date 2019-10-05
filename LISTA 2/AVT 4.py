print("Calcule o peso ideal!")
H = float(input("Digite a sua altura em metros:"))
S = int(input("Digite 1 se for homem ou 2 se for mulher:"))
if S == 1:
    print("Seu peso ideal é:", (72.7 * H) - 58, "kg")
else:
    print("Seu peso ideal é:", (62.1 * H) - 44.7, "kg")