faixa_salarial = float(input("Digite o valor salarial: "))
if faixa_salarial <= 600:
    aumento = faixa_salarial + (faixa_salarial * 0.30)
    print("O novo salário é: " "R$ " '{:.2f}'.format(aumento))
else:
    if faixa_salarial <= 1100:
        aumento_1 = faixa_salarial + (faixa_salarial * 0.25)
        print("O novo salário é: " "R$ ", aumento_1)
    else:
        if faixa_salarial <= 2400:
            aumento_2 = faixa_salarial + (faixa_salarial * 0.20)
            print("O novo salário é: " "R$ ", aumento_2)
        else:
            if faixa_salarial <= 3550:
                aumento_3 = faixa_salarial + (faixa_salarial * 0.15)
                print("O novo salário é: " "R$ ", aumento_3)
            else:
                if faixa_salarial > 3550:
                    aumento_4 = faixa_salarial + (faixa_salarial * 0.10)
                    print("O novo salário é: " "R$ ", aumento_4)
                else:
                    None