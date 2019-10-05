A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
if A < B:
    A = A
    print("O valor crescente é ", A, "e", B)
else:
    A > B
    A = A + B
    B = A - B
    A = A - B
    print("O valor crescente é ", A, "e", B)