#
# Autor: Michel
#
# Data: 10/01/2023

# parte 2:
# usando o python crie um jogo da velha:

#Iniciando a board com espaços vazios
board = [" "," "," "," "," "," "," "," "," "," "]

def tabuleiro():
    # Desenhando o tabuleiro
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("---+---+---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("---+---+---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    
board2 = [" ","1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 "]
def tabuleiroErro():
    # Desenhando o tabuleiro
    print(" " + board2[1] + " | " + board2[2] + " | " + board2[3] + " ")
    print("---+---+---")
    print(" " + board2[4] + " | " + board2[5] + " | " + board2[6] + " ")
    print("---+---+---")
    print(" " + board2[7] + " | " + board2[8] + " | " + board2[9] + " ")

def play():
    # jogada
    turn = "X"
    count = 0
    
    print("Mapa do jogo: (1..9)")
    tabuleiroErro()
    print()


    for i in range(10):
        tabuleiro()
        print(turn + "'é a vez. Mover em qual espaço?")
        move = int(input())
        if board[move] == " ":
            board[move] = turn
            count += 1
        else:
            print("Esse lugar já está preenchido. \nMover para qual lugar? \nConforme:")
            tabuleiroErro()
            continue 
        
        # verificando se o jogador ganhou
        if count >= 5:
            if board[1] == board[2] == board[3] != " ": # primeira linha
                tabuleiro()
                print(turn + " Ganhou!\n")
                return
            elif board[4] == board[5] == board[6] != " ": # segunda linha
                tabuleiro()
                print(turn + " Ganhou!\n")
                return
            elif board[7] == board[8] == board[9] != " ": # terceira linha
                tabuleiro()
                print(turn + " Ganhou!\n")
                return
            elif board[1] == board[4] == board[7] != " ": # primeira coluna
                tabuleiro()
                print(turn + " Ganhou!\n")
                return
            elif board[2] == board[5] == board[8] != " ": # segunda coluna
                tabuleiro()
                print(turn + " Ganhou!\n")
                return
            elif board[3] == board[6] == board[9] != " ": # terceira coluna
                tabuleiro()
                print(turn + " Ganhou!\n")
                return
            elif board[1] == board[5] == board[9] != " ": # diagonal
                tabuleiro()
                print(turn + " Ganhou!\n")
                return
            elif board[3] == board[5] == board[7] != " ": # diagonal
                tabuleiro()
                print(turn + " Ganhou!\n")
                return

        # empate
        if count == 9:
            print("O jogo é um empate\n")
            return

        # alternando jogador
        if turn == "X":
            turn = "O"
        else:
            turn = "X"


if __name__ == '__main__':
    play()
