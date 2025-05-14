class Vetor:
    def __init__(self, quantidade_maxima):
        self.quantidade_maxima = quantidade_maxima
        self.elementos = [0] * quantidade_maxima
        self.comprimento = 0

    def inserir(self, posicao, valor):
        if self.comprimento >= self.quantidade_maxima:
            raise Exception("Quantidade máxima atingida")
        if posicao < 0 or posicao > self.comprimento:
            raise IndexError("Posição inválida")
        for i in range(self.comprimento, posicao, -1):
            self.elementos[i] = self.elementos[i - 1]
        self.elementos[posicao] = valor
        self.comprimento += 1

    def remover(self, posicao):
        if posicao < 0 or posicao >= self.comprimento:
            raise IndexError("Posição inválida")
        for i in range(posicao, self.comprimento - 1):
            self.elementos[i] = self.elementos[i + 1]
        self.elementos[self.comprimento - 1] = 0
        self.comprimento -= 1

    def buscar(self, valor):
        for i in range(self.comprimento):
            if self.elementos[i] == valor:
                return i
        return -1

    def obter(self, posicao):
        if posicao < 0 or posicao >= self.comprimento:
            raise IndexError("Posição inválida")
        return self.elementos[posicao]

    def tamanho(self):
        return self.comprimento

    def para_lista(self):
        return [self.elementos[i] for i in range(self.comprimento)]
