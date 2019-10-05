a = int(input("Dê um valor para 'a': "))
b = int(input("Dê um valor para 'b': "))
c = int(input("Dê um valor para 'c': "))
print('A fórmula é: , (b*b - 4*a*c)')
delta = b * b - 4 * a * c
print('Delta é {}'.format(delta))
print("Agora vamos as raízes!!")
x = - b - (delta)**(1/2)/(2*a)
x1 = - b + (delta)**(1/2)/(2*a)
print('x1 = {}, x2 = {}' .format(x1, x))
if delta == 0:
    print("A equação possui raízes reais e iguais!!", delta == 0)
if delta > 0:
 print("A equação possui raízes reais e distintas!!", delta > 0)
else:
    None
    print("A equação não possui raízes!!")