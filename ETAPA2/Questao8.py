
if JOG1.upper() == "P":
    print("Jogador 1 escolheu par!")
else:
    if JOG1.upper() == "I":
        print("Jogador 1 escolheu ímpar!")
    else:
        print("Jogador 2 escolheu par!")
JOG_1 = int(input("Escolha um número: "))
JOG_2 = int(input("Escolha outro número: "))
SOMA = JOG_1 + JOG_2
RESTO = SOMA % 2
if RESTO == 0 and JOG1 == "P":
    print("Jogador 1 escolheu par e venceu!")
else:
    if RESTO != 0 and JOG1 == "I":
        print("Jogador 1 escolheu ímpar e venceu!")
    else:
        if RESTO == 0 and JOG2 == "P":
            print("Jogador 2 escolheu par e venceu!")
        else:
            if RESTO != 0 and JOG2 == "I":
                print("Jogador 2 escolheu ímpar e venceu!")












