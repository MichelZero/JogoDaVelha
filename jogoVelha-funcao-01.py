#
# Autor: Michel
#
# Data: 18/12/2022

# Para criar um jogo da velha em Python, você pode seguir os seguintes passos:

# 1.	Crie uma matriz 3x3 para armazenar os valores das células do jogo da velha. 
# Você pode inicializá-la com todas as células vazias, usando o caractere ' '.
# 2.	Escreva uma função que imprima o jogo da velha na tela. Ela deve 
# percorrer a matriz e imprimir os valores das células, separando-as por | e adicionando 
# linhas horizontais para cada linha da matriz.
# 3.	Escreva uma função que receba a posição (linha e coluna) e o 
# símbolo (X ou O) e atualize a matriz com o novo valor. Ela deve verificar se a posição é válida (ainda não está ocupada) antes de atualizar a matriz.
# 4.	Escreva uma função que verifique se alguém ganhou o jogo. Ela deve 
# verificar as linhas, colunas e diagonais da matriz para ver se algum dos
# símbolos (X ou O) aparece em todas as células de uma linha, coluna ou diagonal.
# 5.	Escreva o loop principal do jogo, que deve solicitar ao 
# jogador qual é a próxima jogada e atualizar a matriz com o novo valor. O loop 
# deve continuar até que alguém ganhe ou até que não hajam mais células vazias (empate).


# Jogo da velha em Python

# Criando a matriz 3x3 vazia
velha = [[' ' for i in range(3)] for j in range(3)]
# ou
# velha = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Função para imprimir o jogo da velha
def imprime_velha():
  print('---------')
  for i in range(3):
    print(f'| {velha[i][0]} {velha[i][1]} {velha[i][2]} |')
  print('---------')

# Função para atualizar a matriz do jogo da velha
def atualiza_velha(linha, coluna, símbolo):
  if velha[linha][coluna] != ' ':
    print('Posição já ocupada! Escolha outra.')
    return
  velha[linha][coluna] = símbolo

# Função para verificar se alguém ganhou o jogo
def verifica_vitória(símbolo):
  # Verificando as linhas
  for i in range(3):
    if velha[i][0] == símbolo and velha[i][1] == símbolo and velha[i][2] == símbolo:
      # return True
      return f'Vencedor:'
    
    
#####################################################################################

imprime_velha()
atualiza_velha(0, 0, 'X')
imprime_velha()
atualiza_velha(0, 1, 'X')
atualiza_velha(0, 2, 'X')
imprime_velha()
verifica_vitória('X')