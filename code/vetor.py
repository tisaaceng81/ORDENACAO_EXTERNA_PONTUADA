class Vetor:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.dados = [None] * capacidade
        self.tamanho_atual = 0

    def inserir(self, posicao, valor):
        if self.tamanho_atual >= self.capacidade:
            raise Exception("Capacidade máxima atingida")
        if posicao < 0 or posicao > self.tamanho_atual:
            raise IndexError("Posição inválida")
        for i in range(self.tamanho_atual, posicao, -1):
            self.dados[i] = self.dados[i - 1]
        self.dados[posicao] = valor
        self.tamanho_atual += 1

    def remover(self, posicao):
        if posicao < 0 or posicao >= self.tamanho_atual:
            raise IndexError("Posição inválida")
        for i in range(posicao, self.tamanho_atual - 1):
            self.dados[i] = self.dados[i + 1]
        self.dados[self.tamanho_atual - 1] = None
        self.tamanho_atual -= 1

    def buscar(self, valor):
        for i in range(self.tamanho_atual):
            if self.dados[i] == valor:
                return i
        return -1

    def obter(self, posicao):
        if posicao < 0 or posicao >= self.tamanho_atual:
            raise IndexError("Posição inválida")
        return self.dados[posicao]

    def tamanho(self):
        return self.tamanho_atual

    def para_lista(self):
        return [self.dados[i] for i in range(self.tamanho_atual)]
