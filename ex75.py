




def dados(valores):
    print(f'o valor 9 apareceu {valores.count(9)} vezes')
    
    if 3 in valores:
     print(f'O valor 3 apareceu {valores.index(3) + 1} ª posição')
    else:
        print('O valor 3 não foi digitado em nenhuma posição')
    
    for i in valores:
        if i % 2 == 0:
            print(f'{i}', end= " ")
    





 # Programa Principal !
valores = tuple (int(input('Digite 4 números'))for i in range( 1 , 5))
dados(valores)

