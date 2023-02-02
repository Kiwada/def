#Faça um programa que tenha uma lista chamada números e duas funçoes
#Chamadas sorteia() e somaPar().A primeira função vai sortear 5 números 
#E vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
#Os valores Pares Sorteados pela função Anterior.
from random import randint





def sorteia(lista):
    print('Sorteando 5 valores da lista: ' , end = '')
    for i in range(0,5):
        n = randint(1,1000)
        lista.append(n)
        print(f'{n}', end =' ', flush= True)
    print('Pronto!')
        


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
         soma += valor
    print(f'Somando os valores de {lista} , temos {soma}')




#Programa Principal
Número = list()
sorteia(Número) 
somaPar(Número)


