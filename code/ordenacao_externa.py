import time
from vetor import Vetor

class OrdenacaoExterna:
    def __init__(self, elementos, limite_memoria=6, atraso=0.3, tamanho_blocos=2):
        if tamanho_blocos > limite_memoria:
            print(f"[AVISO] Tamanho de bloco ({tamanho_blocos}) não suportado pela memória ({limite_memoria}).")
            print(f"[AÇÃO] Ajustando tamanho do bloco para {limite_memoria}.\n")
        self.elementos = elementos
        self.limite_memoria = limite_memoria
        self.atraso = atraso
        self.sublistas = Vetor(len(elementos))  # Substituição de lista padrão
        self.passadas_intercalacao = 0
        self.passadas_merge_sort = 0
        self.comparacoes_merge_sort = 0
        self.tamanho_blocos = min(tamanho_blocos, self.limite_memoria)

    def _ler_bloco(self, elementos, inicio, tamanho):
        bloco = Vetor(min(tamanho, len(elementos) - inicio))
        for i in range(bloco.quantidade_maxima):
            bloco.inserir(i, elementos[inicio + i])
        print(f"Lendo bloco: {bloco.para_lista()}")
        time.sleep(self.atraso)
        return bloco

    def _intercalar_duas_listas(self, v1, v2):
        print(f"-> Junção: {v1.para_lista()} + {v2.para_lista()}")
        resultado = Vetor(v1.tamanho() + v2.tamanho())
        i = j = 0
        while i < v1.tamanho() and j < v2.tamanho():
            self.comparacoes_merge_sort += 1
            if v1.obter(i) <= v2.obter(j):
                resultado.inserir(resultado.tamanho(), v1.obter(i))
                i += 1
            else:
                resultado.inserir(resultado.tamanho(), v2.obter(j))
                j += 1
            time.sleep(self.atraso)
        while i < v1.tamanho():
            resultado.inserir(resultado.tamanho(), v1.obter(i))
            i += 1
        while j < v2.tamanho():
            resultado.inserir(resultado.tamanho(), v2.obter(j))
            j += 1
        print(f"-> Resultado da junção: {resultado.para_lista()}")
        return resultado

    def _merge_sort(self, vetor):
        self.passadas_merge_sort += 1
        print(f"Passada Merge Sort {self.passadas_merge_sort}: {vetor.para_lista()}")
        if vetor.tamanho() <= 1:
            return vetor

        meio = vetor.tamanho() // 2
        esquerda = Vetor(meio)
        direita = Vetor(vetor.tamanho() - meio)

        for i in range(meio):
            esquerda.inserir(i, vetor.obter(i))
        for i in range(meio, vetor.tamanho()):
            direita.inserir(i - meio, vetor.obter(i))

        # Comparação simples entre extremos
        if esquerda.obter(esquerda.tamanho() - 1) > direita.obter(0):
            print("Comparando extremidades: esquerda > direita")
        elif esquerda.obter(esquerda.tamanho() - 1) < direita.obter(0):
            print("Comparando extremidades: esquerda < direita")
        else:
            print("Comparando extremidades: esquerda == direita")

        return self._intercalar_duas_listas(
            self._merge_sort(esquerda),
            self._merge_sort(direita)
        )

    def gerar_sublistas(self):
        print("=== FASE 1: Geração de sublistas ===")
        for i in range(0, len(self.elementos), self.tamanho_blocos):
            bloco = self._ler_bloco(self.elementos, i, self.tamanho_blocos)
            print(f"-> Ordenando bloco com Merge Sort: {bloco.para_lista()}")
            bloco_ordenado = self._merge_sort(bloco)
            print(f"-> Bloco ordenado: {bloco_ordenado.para_lista()}")
            self.sublistas.inserir(self.sublistas.tamanho(), bloco_ordenado)

    def intercalar_sublistas(self):
        print("\n=== FASE 2: Junção das sublistas ===")
        while self.sublistas.tamanho() > 1:
            novas_sublistas = Vetor(self.sublistas.tamanho() // 2 + 1)
            i = 0
            while i < self.sublistas.tamanho():
                if i + 1 < self.sublistas.tamanho():
                    sub1 = self.sublistas.obter(i)
                    sub2 = self.sublistas.obter(i + 1)
                    time.sleep(self.atraso)
                    intercalada = self._intercalar_duas_listas(sub1, sub2)
                    time.sleep(self.atraso)
                    novas_sublistas.inserir(novas_sublistas.tamanho(), intercalada)
                    self.passadas_intercalacao += 1
                else:
                    novas_sublistas.inserir(novas_sublistas.tamanho(), self.sublistas.obter(i))
                i += 2
            self.sublistas = novas_sublistas

    def _exibir_resultado(self, resultado, tempo_total):
        print("\n=== RESULTADO FINAL ===")
        print(f"Lista ordenada: {resultado.para_lista()}")
        print(f"Passadas de junção: {self.passadas_intercalacao}")
        print(f"Passadas de Merge Sort: {self.passadas_merge_sort}")
        print(f"Comparações no Merge Sort: {self.comparacoes_merge_sort}")
        print(f"Tempo total: {tempo_total:.2f} segundos")

    def ordenar(self):
        print("=== INICIANDO ORDENAÇÃO EXTERNA ===")
        print(f"Limite de memória: {self.limite_memoria}")
        print(f"Tamanho dos blocos: {self.tamanho_blocos}")
        print(f"Atraso entre passos: {self.atraso} segundos")
        print(f"Tamanho total dos dados: {len(self.elementos)}")
        print("=" * 40)

        inicio = time.time()
        self.gerar_sublistas()
        self.intercalar_sublistas()
        resultado_final = self.sublistas.obter(0) if self.sublistas.tamanho() > 0 else Vetor(0)
        fim = time.time()
        self._exibir_resultado(resultado_final, fim - inicio)
        return resultado_final.para_lista()
