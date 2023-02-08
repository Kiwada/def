
c = 0
num = ()
for n in range(0, 4):
    n = int(input('Digite um número entre 1 e 10: '))
    while n < 1 or n > 10:
        n = int(input('Tente novamente. Digite um número entre 1 e 10: '))
    num += (n,) # acrescenta valores em uma tupla quando ela está dentro de um laço.
print(f'Os quatro valores digitados foram: {num}')
if num.count(9) >= 1:
    print(f"O número 9 apareceu {num.count(9)} vez(es).")
else:
    print('Não há nenhum número 9 entre os valores.')
if num.count(3) >= 1:
    print(f'O primeiro número 3 está na {num.index(3) + 1}ª posição.')
else:
    print('Não há nenhum número 3 entre os valores.')
print('Os números pares são: ', end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')
    else:
        c += 1
        if c == 4:
            print('nenhum')