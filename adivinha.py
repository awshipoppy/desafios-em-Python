import random

print(f'Olá! Você pode tentar adivinhar o número que estou pesando?')

while True:
    print(f'Fale o valor máximo para eu não ultrapassa-lo (ou sair)')
    vlr = input('Valor = ')
    if vlr == 'sair':
        break
    vlr = int(vlr)
    vlr_aleatorio = random.randrange(1, vlr+1)
    print(f'Qual é o número que pensei?')
    vlr = int(input('Coloque = '))
    if vlr == vlr_aleatorio:
        print(f'Você acertou!')
    else:
        print(f'Muito ruim, eu pensei no {vlr_aleatorio}')