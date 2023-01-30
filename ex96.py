#ex96
#Faça um Programa que tenha uma função chamada Area() de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def linnha():
    print('Controle de Terrenos')
    print('-=-'*10)

def área(L,C):
    A = L*C
    print(f'A àrea de um terreno {L} x {C} é de {A} ')


#Programa Principal
linha()
L = float(input('Largura(m)'))
C = float(input('Comprimento(m):'))
área(L,C)




#def area(larg, comp):
#    a = larg * comp
#    print(f'área de um terreno {larg} x{comp} é de {a}m2.')

#programa principal
#   print('controle de terrenos')
#   print('-' *30)
# l = float(input('Largura(M):))
# c = float(input('COMRPIMENTO(M):))
# area(l,c)
