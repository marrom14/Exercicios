nome = input("Digite o seu nome: ")
nota_1 = int(input("Sua nota na matéria A: "))
nota_2 = int(input("Sua nota na matéria B: "))
nota_3 = int(input("Sua nota na matéria C: "))
numero_faltas = int(input("Número de faltas: "))
media_aprovação = int(nota_1 + nota_2 + nota_3) / 3
total_faltas = numero_faltas * 100 / 80
if total_faltas < 25 and media_aprovação >= 7:
    print("Aluno", nome, "foi aprovado!!!")
else:
    if total_faltas > 25:
        print("Aluno", nome, "foi reprovado por excesso de faltas!!!")
    else:
        if media_aprovação < 7:
            print("Aluno", nome, "foi reprovado por não alcançar a média!!!")
        else:
            None