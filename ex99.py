#ex99
#Faça um programa que tenha uma função chamada maior(), que 
#uma função chamada maior(),que receba vários parâmetros com 
#valores inteiros. Seu programa tem que analisar  todos os valores e dizer 
#qual deles é o maior.
from time import sleep




def maior(* num):
    cont = maior = 0
    print ('\n Analisando os Valores')
    for valor in num :
      print(f'{valor}' , end = ' ', flush= True)
      sleep(0.3)
      if cont == 0 :                              #se eu não tenho número nenhum ainda para ser analísado ele é o maior
        maior = valor                             # ele é o maior
      else :                                      #senão
         if valor > maior :                       #vou verificar se o valor for maior for ( MAIOR QUE O MAIOR VALOR)
            maior = valor                         # o maior valor passa a ser o maior
            cont += 1
    

    print(f'Foram Informado {cont} valores')
    print(f'O maior valor informado foi {maior}')



    


##Programa Principal
maior( 2 , 9 , 5 , 7 , 1)
