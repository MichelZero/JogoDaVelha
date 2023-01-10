#
# Autor: Michel
#
# Data: 21/12/2022

# parte 1:
# usando o python crie um jogo da velha:

# Criando a matriz 3x3 vazia
velha = [[' ' for i in range(3)] for j in range(3)]

# função para imprimir o jogo da velha
def imprime_velha():
  print('-------')
  for i in range(3):
    print(f'|{velha[i][0]} |{velha[i][1]} |{velha[i][2]}')
  print('-------')

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
  
#####################################################################################
# testando o código

imprime_velha()
tabuleiro()
tabuleiroErro()