lista = []
for n in range(4):
    num = int(input(f'Digite um número para a posição {n}:'))
    lista.append(num)

maior = menor = lista[0]


for i in lista[1:]:
    if i < menor:
        menor = i
    if i > maior:
        maior = i

print(f'O maior valor informado foi : {maior} e sua posição é { lista.index(maior)}')
print(f'O menor valor informado foi : {menor} e sua posição {lista.index(menor)}')