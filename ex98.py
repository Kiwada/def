from time import sleep


def escreva(msg):
    tam = len(msg) + 4
    print('=' * tam)
    print(f'  {msg}  ')
    print('='*tam)
def contador (i , f , p):
    if p < 0 :
        p *= -1
    if p == 0 :
        p = 1
   
    print(f'contagem de {i} até {f} de {p} em {p}')
    sleep(0.8)
   
    
    if i < f:
        cont = i 
        while cont <= f:
            print(f'{cont}' , end=' ', flush = True)
            sleep(0.1)
            cont += p
        print(' FIM')
    else:
        cont = i 
        while cont >= f:
            print(f'{cont}' , end=' ', flush = True)
            sleep(0.1)
            cont -= p
        print('FIM !')


contador(1, 10, 1)
contador(10 , 32 ,1)
escreva('Agora é sua vez de personalizar a contagem !')
ini = int(input('inicio'))
fim = int(input('fim'))
pas = int(input('passos'))
contador (ini , fim , pas)
