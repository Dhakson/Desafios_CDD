from random import randint
import time


while True:
    print("JOGO DO PEDRA, PAPEL E TESOURA")
    print("VAMOS JOGAR")
    print("Pedra ✊")
    time.sleep(1)
    print("Papel 🖐️")
    time.sleep(1)
    print("Tesoura ✌️")
    time.sleep(1)
    print()
    print("[1] - PEDRA \n[2] - PAPEL \n[3] - TESOURA")
    jogador = 0
    jogadas = {1: "Pedra ✊", 2: "Papel 🖐️", 3: "Tesoura ✌️"}
    while jogador not in jogadas:
        jogador = int(input("Escolha a opção: "))
        if jogador not in jogadas:
            print("Joga Invalida tente novamente")

    print("Agora é a vez do Computador")
    time.sleep(1)
    computador = randint(1, 3)
    time.sleep(1)
    print("O Computador Jogou")
    print()
    print("=" * 30)
    print(f'O Jogador Jogou: {jogadas[jogador]}')
    print(f'O Comoutador Jogou: {jogadas[computador]}')
    print("=" * 30)

    if jogador == computador:
        print('Jogo Empatado')

    elif (jogador == 1 and computador == 3) or \
            (jogador == 2 and computador == 1) or \
            (jogador == 3 and computador == 2):
        print("Jogador ganhou")
        break
    elif (jogador == 3 and computador == 1) or \
            (jogador == 1 and computador == 2) or \
            (jogador == 2 and computador == 3):
        print("Computador Ganhou")






    resp = input("Quer Continuar Sim ou Não: ").strip().lower()
    if resp != "s":
        break