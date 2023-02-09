#Faça um programa que leia 5 valores numéricos e guarde-os em 
#uma lista. No final, mostre qual foi o maior e o menor valor
#digitado e as suas respectivas posições na lista.

listanum = []        #declarei que listanum é a lista []

maior =  0            #atribui o valor de 0 para o maior
menor =   0            #atribui o valor de 0 para o menor
for pos in range( 0, 5):      #estrutura de repetição com váriavel de controle (de 1 a 5)
    listanum.append(int(input(f'digite um valor para a posição {pos} :'))) # Acrescenta um item ao fim da lista. Equivalente a a[len(a):] = [x]
    if pos == 0:  #se a posição for igual a zero
        maior = menor = listanum[pos] #o maior vai atribuir o valor do menor e depois ser acrescentado na posição
    else:                         #senão , entra em mais um teste condicional
        if listanum[pos] > maior:   #se a posição dentro da lista for maior que o MAIOR
            maior = listanum[pos]   #o maior atribui a posição
        if listanum[pos] < menor : #se a posição for menor que o menor número
            menor = listanum[pos]  #o menor atribui a a posição

print(f' Você digitou os valores {listanum}') #valores da lista
print(f' O menor valor digitado foi {menor} na posição ' , end = '')
for pos , v in enumerate(listanum):  # para cada posição e valor na lista num
    if v == menor :
        print(f'{pos }')
print(f'O maior valor foi  {maior} na posição ' , end= '')
for pos , v in enumerate(listanum):
    if v == maior:
        print(f'{pos}')
    