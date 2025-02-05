import random

def criar_tabuleiro(tamanho, num_minas):
    tabuleiro = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]
    minas = set()
    while len(minas) < num_minas:
        x, y = random.randint(0, tamanho - 1), random.randint(0, tamanho - 1)
        minas.add((x, y))
    return tabuleiro, minas

def contar_minas_vizinhas(tabuleiro, minas, x, y):
    direcoes = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    contagem = 0
    for dx, dy in direcoes:
        if (x + dx, y + dy) in minas:
            contagem += 1
    return contagem

def revelar_celula(tabuleiro, minas, x, y, reveladas):
    if (x, y) in minas:
        return False
    if (x, y) in reveladas:
        return True
    reveladas.add((x, y))
    num_minas = contar_minas_vizinhas(tabuleiro, minas, x, y)
    tabuleiro[x][y] = str(num_minas) if num_minas > 0 else '.'
    if num_minas == 0:
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(tabuleiro) and 0 <= ny < len(tabuleiro):
                revelar_celula(tabuleiro, minas, nx, ny, reveladas)
    return True

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' '.join(linha))

def jogo_campo_minado(tamanho=5, num_minas=5):
    tabuleiro, minas = criar_tabuleiro(tamanho, num_minas)
    reveladas = set()
    
    while len(reveladas) < tamanho * tamanho - num_minas:
        imprimir_tabuleiro(tabuleiro)
        try:
            x, y = map(int, input("Digite as coordenadas (linha coluna): ").split())
            if not (0 <= x < tamanho and 0 <= y < tamanho):
                print("Coordenadas fora dos limites!")
                continue
            if not revelar_celula(tabuleiro, minas, x, y, reveladas):
                print("Você acertou uma mina! Game Over.")
                return
        except ValueError:
            print("Entrada inválida! Digite dois números separados por espaço.")
    
    print("Parabéns! Você venceu o jogo!")
    imprimir_tabuleiro(tabuleiro)

if __name__ == "__main__":
    jogo_campo_minado()
