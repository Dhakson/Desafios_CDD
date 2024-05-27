class Jogo():
    def __init__(self):
        self.tabuleiro = [" "] * 9
        self.player1 = 'X'
        self.player2 = "O"
        self.turno = False
        self.jogadas = 0
    def imprimir_tabuleiro(self):
        print(f"{self.tabuleiro[0]} | {self.tabuleiro[1]} | {self.tabuleiro[2]}")
        print("---------")
        print(f"{self.tabuleiro[3]} | {self.tabuleiro[4]} | {self.tabuleiro[5]}")
        print("---------")
        print(f"{self.tabuleiro[6]} | {self.tabuleiro[7]} | {self.tabuleiro[8]}")

    def jogada(self):
        while self.jogadas < 9:
            self.imprimir_tabuleiro()

            if self.turno:
                self.player = self.player2
                self.player_num = 2
            else:
                self.player = self.player1
                self.player_num = 1

            try:
                self.posicao = int(input(f"Informe a sua Player{self.player_num} jogada de 0 a 8: "))
                if self.jogadas < 0 or self.jogadas >8:
                    print("Posição Invalida!")
                    continue
            except ValueError:
                print("Numero Invalido. Jogue de 0 a 8! ")
                continue

            if self.tabuleiro[self.posicao] == " ":
                self.tabuleiro[self.posicao] = self.player
                self.jogadas += 1
            else:
                print("Casa Já preenchida tente novamente")
                continue

            if self.verificar_vencedor():
                self.imprimir_tabuleiro()
                print(f"O Jogador{self.player_num} {self.player} Venceu!")
                break

            self.turno = not self.turno

        if self.jogadas == 0:
            self.imprimir_tabuleiro()
            print("O jogou terminou em empate")


    def verificar_vencedor(self):
        for i in range(0,9,3):
            if self.tabuleiro[i] == self.tabuleiro[i+1] == self.tabuleiro[i+2] != " ":
                return True

        for i in range(3):
            if self.tabuleiro[i] == self.tabuleiro[i+3] == self.tabuleiro[i+3] != " ":
                return True

        if self.tabuleiro[0] == self.tabuleiro[4] == self.tabuleiro[8] != " ":
            return True

        if self.tabuleiro[2] == self.tabuleiro[4] == self.tabuleiro[6] != " ":
            return True


