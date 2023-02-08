#76
# Crie um programa que tenha uma tupla única com nomes de
# produtos e seus respectivos preços, na sequenência.
#No final. moste uma listagem de preços, organizando os dados em
# forma tabular.

def escreva(msg):
    tam = len(msg)+30
    print('=' * tam)
    print(f'{msg:^{tam}}')
    print('=' * tam)





def tabular(tabela):
    for pos in range (0, len(tabela)):
        if pos % 2 == 0:
            print(f'{tabela[pos]:.<30}', end = '') 
        else:
            print(f'R$  {tabela[pos]}:')



escreva('Lista De Coisas')

tabela = ('Caneta', 1.0, 'Lapis', 5.0, 'Borracha', 0.5, 'Caderno', 20.0, 'Fichário', 29.99)
tabular(tabela)
