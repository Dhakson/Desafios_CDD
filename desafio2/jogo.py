from random import *
from time import sleep
class Ppt():
    def __init__(self):
        self.jogador = 0
        #O computador joga aleatorio
        self.computador = randint(1,3)
        #Usei um dicionário a onde transforma número em STR
        self.jogadas = {1: "Pedra ✊", 2: "Papel 🖐️", 3: "Tesoura ✌️"}

    def menu(self):
        #Menu de exibição para o usuário ver em qual jogada fará
        print("JOGO DA PEDRA,PAPEL e TESOURA")
        print("[1] - Pedra ✊")
        sleep(1)
        print("[2] - Papel 🖐️")
        sleep(1)
        print("[3] - Tesoura ✌️")
        sleep(1)
    def jogador1(self):
        while True:
            # Tratamento de erro caso o usuário não digite de 1 a 3.
            try:
                self.jogador = int(input("Sua Jogada de 1 a 3: "))
                if self.jogador in self.jogadas:
                    print(f'O jogador jogou {self.jogadas[self.jogador]}')
                    break
                else:
                    print("Jogada Invalida. Tente novamente")
            except ValueError:
                print("Escolha de 1 a 3!")

    def jogador2(self):
        #Aqui o computador joga aleatoriamente de 1 a 3 através do randint
        self.computador = self.computador
        print(f'O computador Jogou {self.jogadas[self.computador]}')

    def resultado(self):
        #Aqui verifica se as jogadas foram iguais
        # jogador ganhou ou perdeu pro computador
        if self.jogador == self.computador:
            print("Jogada Empatada")
        elif (self.jogador == 1 and self.computador == 3) or \
                (self.jogador == 2 and self.computador == 1) or \
                (self.jogador == 3 and self.computador == 2):
            print("Jogador Ganhou a Partida")
        else:
            print("Computador Ganhou a Partida")
