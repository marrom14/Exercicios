HOMEM_VELHO = int(input("Informe a primeira idade: "))
HOMEM_NOVO = int(input("Informe a segunda idade: "))
MULHER_VELHA = int(input("Informe a terceira idade: "))
MULHER_NOVA = int(input("Informe a quarta idade: "))
HOMEM_VELHO != HOMEM_NOVO and MULHER_VELHA != MULHER_NOVA
if HOMEM_VELHO > HOMEM_NOVO and MULHER_VELHA > MULHER_NOVA:
    soma = HOMEM_VELHO + MULHER_NOVA
else:
    soma = HOMEM_NOVO + MULHER_VELHA
print("A soma das idades do homem mais velho com a mulher mais nova é: ", soma)
if HOMEM_VELHO > HOMEM_NOVO and MULHER_VELHA > MULHER_NOVA:
    produto = HOMEM_NOVO * MULHER_VELHA
else:
    produto = HOMEM_VELHO * MULHER_NOVA
print("O produto das idades do homem mais novo com a mulher mais velha é: ", produto)