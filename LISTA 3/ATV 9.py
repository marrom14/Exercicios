lado_A = int(input("Informe o número do lado A: "))
lado_B = int(input("Informe o número do lado B: "))
lado_C = int(input("Informe o número do lado C: "))
if lado_A == lado_B == lado_C:
    print("Formou-se os lados de um triângulo Equilátero!!!")
else:
    if lado_A == lado_B or lado_A == lado_C or lado_B == lado_C:
        print("Formou-se os lados de um triângulo Isósceles!!!")
    else:
        print("Formou-se os lados de um triângulo Escaleno!!!")