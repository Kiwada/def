#Exercício Python 077: Crie um programa que tenha uma tupla com várias
#palavras (não usar acentos). Depois disso, você deve mostrar, para cada
#palavra, quais são as suas vogais.
def vogais(palavra):
    for p in palavra:
        print(f' \n Na Palavra {p}' , end = '')
        for letra in p:
           if letra.lower() in'aeiou':
             print(f'{letra}' , end = ' ' )








palavras = tuple(str(input('Digite Palavras Para Descobrir as Vogais !'))for i in range(0,2))
vogais(palavras)