tabuleiro = [" "]*9

player1 = "X"
player2 = "O"

turno = False
jogadas = 0
while jogadas < 9:
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("---------")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("---------")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

    if turno:
        player = player2
        player_num = 2
    else:
        player = player1
        player_num = 1


    try:
        posicao = int(input(f"Jogador Nª{player_num}, qual será a sua jogada de [0-8]: "))
        if posicao < 0 or posicao > 8:
            print("Posição Invalida.Tente novamente!")
            continue
    except ValueError:
        print("Entrada Invalida.Digite um número de 0 a 8.")
        continue

    if tabuleiro[posicao] == " ":
        tabuleiro[posicao] = player
        jogadas += 1
    else:
        print("Casa Preenchida, tente novamente.")

    for c in range(0,9,3):
        if tabuleiro[c] == tabuleiro[c+1] == tabuleiro[c+2] != " ":
            print(f"O jogador {player} venceu na Horizontal")
            break

    for c in range(3):
        if tabuleiro[c] == tabuleiro[c+3] == tabuleiro[c+6] != " ":
            print(f"O jogador {player} venceu na Vertical")
            break

    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != " ":
        print(f"O jogador {player} venceu na Diagonal")
        break

    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != " ":
        print(f"O jogador {player} venceu na Diagonal")
        break


    turno = not turno