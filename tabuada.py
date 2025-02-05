#Código em Pytho mostrando a taubada de um número de 0 a 10
print(f"Olá! Te mostrarei a tabuada de 1 a 10 de um número a sua escolha!")
while True:
    num = int(input('Diga um número inteiro a sua escolha: '))
    control = 1
    while control <= 10:
        print(f'{control} * {num} é: {num*control}')
        control = control + 1
    esc = input('Desejar sair? (Sim) ou (Não) = ')
    if esc == 'Sim':
        break