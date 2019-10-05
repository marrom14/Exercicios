print("Qual área você deseja calcular?")
tipo = input("Digite (T)riângulo, (Q)uadrado ou (C)írculo: ")
if tipo.upper() == "T":
    base_triangulo = int(input("Informe a base do triângulo: "))
    altura_triangulo = int(input("Informe a altura do triângulo: "))
    area_triangulo = (base_triangulo * altura_triangulo) / 2
    print("Como você escolheu Triângulo, sua área é ",area_triangulo, "m²")
if tipo.upper() == "Q":
    lado_1 = int(input("Informe o lado do quadrado: "))
    area_quadrado = lado_1 * lado_1
    print("Como você escolheu Quadrado, sua área é ", area_quadrado, "m²")
if tipo.upper() == "C":
    raio = int(input("Informe o raio do Círculo: "))
    area_circulo = 3.14 * (raio**2)
    print("Como você escolheu Círculo, sua área é", area_circulo, "m²")