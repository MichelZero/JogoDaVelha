#
# Autor: Michel
#
# Data: 18/12/2022

# Para criar um jogo da velha em Python, você pode seguir os seguintes passos:

# 1. Defina a classe JogoDaVelha e crie um construtor para inicializar o estado do 
# jogo. Você pode usar uma lista de strings para representar o tabuleiro, 
# onde cada string é uma linha do tabuleiro e cada caractere é um quadrado. 
# Você também pode incluir um atributo para armazenar o jogador atual (X ou O).

# 2. Crie um método jogar() para realizar uma jogada. Este método deve receber 
# as coordenadas da jogada (linha e coluna) e atualizar o estado do jogo de 
# acordo. Certifique-se de verificar se a jogada é válida (por exemplo, 
# se o quadrado já está ocupado).

# 3. Crie um método fim_de_jogo() para verificar se o jogo terminou. 
# Isso pode ser feito verificando se houve um vencedor (todos os quadrados 
# de uma linha, coluna ou diagonal são ocupados pelo mesmo jogador) 
# ou se o tabuleiro está completamente preenchido sem um vencedor (empate).

# 4. Crie um método imprimir_tabuleiro() para exibir o estado atual do jogo. 
# Isso pode ser feito usando a lista de strings que representa o tabuleiro.

# 5. No seu programa principal, crie uma instância da classe JogoDaVelha e 
# inicie o jogo. Peça ao jogador para fornecer as coordenadas da próxima 
# jogada e chame o método jogar() até que o jogo termine. Em seguida, 
# exiba uma mensagem indicando o resultado do jogo.

# Um exemplo de código que implementa um jogo da velha em Python:

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [' '] * 9
        self.jogador_atual = 'X'

    def jogar(self, linha, coluna):
        indice = 3 * linha + coluna
        if self.tabuleiro[indice] != ' ':
            raise ValueError("Quadrado já ocupado")
        self.tabuleiro[indice] = self.jogador_atual
        if self.jogador_atual == 'X':
            self.jogador_atual = 'O'
        else:
            self.jogador_atual = 'X'

    def fim_de_jogo(self):
        # verifica se houve um vencedor
        for i in range(3):
            if self.tabuleiro[3*i] == self.tabuleiro[3*i+1] == self.tabuleiro[3*i+2] != ' ':
                # return True
                return f'Vencedor:'


###################################################
jv1 = JogoDaVelha()
jv1.jogar(0, 0)
jv1.jogar(0, 1)
jv1.jogar(1, 0)
jv1.jogar(1, 1)
jv1.jogar(2, 0)
jv1.jogar(2, 1)
jv1.jogar(0, 2)
jv1.jogar(1, 2)
jv1.jogar(2, 2)
fim = jv1.fim_de_jogo
print(fim)