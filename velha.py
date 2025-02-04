import random

print('Bem-vindo! Vamos jogar Pedra, Papel ou Tesoura.')

opcoes = ['Pedra', 'Papel', 'Tesoura']

while True:
    esc = input('Escolha Pedra, Papel ou Tesoura (ou "sair" para encerrar): ').capitalize()

    if esc == 'Sair':
        print('Obrigado por jogar! Até a próxima.')
        break

    if esc not in opcoes:
        print('Escolha inválida! Tente novamente.')
        continue

    esc_com = random.choice(opcoes)
    print(f'O computador escolheu: {esc_com}')

    if esc == esc_com:
        print('Ocorreu um empate!')
    elif (esc == 'Pedra' and esc_com == 'Tesoura') or \
         (esc == 'Papel' and esc_com == 'Pedra') or \
         (esc == 'Tesoura' and esc_com == 'Papel'):
        print('Você venceu!')
    else:
        print('O computador venceu!')

    print('-' * 30)
