def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all([celula == jogador for celula in linha]):
            return True
    for coluna in range(3):
        if all([tabuleiro[linha][coluna] == jogador for linha in range(3)]):
            return True
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True
    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    jogador_atual = 0
    jogadas = 0

    while True:
        imprimir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogadores[jogador_atual]}, escolha a linha (0, 1 ou 2): "))
        coluna = int(input(f"Jogador {jogadores[jogador_atual]}, escolha a coluna (0, 1 ou 2): "))
        if tabuleiro[linha][coluna] != " ":
            print("Posição já ocupada. Tente novamente.")
            continue
        tabuleiro[linha][coluna] = jogadores[jogador_atual]
        jogadas += 1
        if verificar_vitoria(tabuleiro, jogadores[jogador_atual]):
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns, jogador {jogadores[jogador_atual]}! Você venceu!")
            break
        if jogadas == 9:
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break
        jogador_atual = 1 - jogador_atual

jogar_jogo_da_velha()
