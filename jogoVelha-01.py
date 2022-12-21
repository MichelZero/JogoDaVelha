#
# Autor: Michel
#
# Data: 21/12/2022

# usando o python crie um jogo da velha:

# Criando a matriz 3x3 vazia
velha = [[' ' for i in range(3)] for j in range(3)]

# função para imprimir o jogo da velha
def imprime_velha():
  print('------------')
  for i in range(3):
    print(f'|__{velha[i][0]}|__{velha[i][1]}|__{velha[i][2]}|')
  print('------------')
  
#####################################################################################
# testando o código

imprime_velha()