import time
from vetor import Vetor

class OrdenacaoExterna:
    def __init__(self, dados, limite_memoria=6, atraso=0.3, tamanho_blocos=2):
        if tamanho_blocos > limite_memoria:
            print(f"[AVISO] Tamanho de bloco ({tamanho_blocos}) não suportado pela memória ({limite_memoria}).")
            print(f"[AÇÃO] Ajustando tamanho do bloco para {limite_memoria}.\n")
        self.dados = dados
        self.limite_memoria = limite_memoria
        self.atraso = atraso
        self.sublistas = []
        self.passadas_intercalacao = 0
        self.passadas_merge_sort = 0
        self.comparacoes_merge_sort = 0  # Contador de comparações
        self.tamanho_blocos = min(tamanho_blocos, self.limite_memoria)

    def _ler_bloco(self, dados, inicio, tamanho):
        bloco = dados[inicio:inicio + tamanho]
        print(f"Lendo bloco: {bloco}")
        time.sleep(self.atraso)
        return bloco

    def _intercalar_duas_listas(self, lista1, lista2):
        print(f"-> Junção: {lista1} + {lista2}")
        resultado = Vetor(len(lista1) + len(lista2))
        i = j = 0
        while i < len(lista1) and j < len(lista2):
            self.comparacoes_merge_sort += 1
            if lista1[i] <= lista2[j]:
                resultado.inserir(resultado.tamanho(), lista1[i])
                i += 1
            else:
                resultado.inserir(resultado.tamanho(), lista2[j])
                j += 1
            time.sleep(self.atraso)
        while i < len(lista1):
            resultado.inserir(resultado.tamanho(), lista1[i])
            i += 1
        while j < len(lista2):
            resultado.inserir(resultado.tamanho(), lista2[j])
            j += 1
        resultado_lista = resultado.para_lista()
        print(f"-> Resultado da junção: {resultado_lista}")
        return resultado_lista

    def _merge_sort(self, lista):
        self.passadas_merge_sort += 1
        print(f"Passada Merge Sort {self.passadas_merge_sort}: {lista}")
        if len(lista) <= 1:
            return lista

        meio = len(lista) // 2
        esquerda = self._merge_sort(lista[:meio])
        direita = self._merge_sort(lista[meio:])

        # Comparação simples entre extremos
        if max(esquerda) > min(direita):
            print("Comparando extremidades: esquerda > direita")
        elif max(esquerda) < min(direita):
            print("Comparando extremidades: esquerda < direita")
        else:
            print("Comparando extremidades: esquerda == direita")

        return self._intercalar_duas_listas(esquerda, direita)

    def gerar_sublistas(self):
        print("=== FASE 1: Geração de sublistas ===")
        for i in range(0, len(self.dados), self.tamanho_blocos):
            bloco = self._ler_bloco(self.dados, i, self.tamanho_blocos)
            print(f"-> Ordenando bloco com Merge Sort: {bloco}")
            bloco_ordenado = self._merge_sort(bloco)
            print(f"-> Bloco ordenado: {bloco_ordenado}")
            vetor = Vetor(len(bloco_ordenado))
            for valor in bloco_ordenado:
                vetor.inserir(vetor.tamanho(), valor)
            self.sublistas.append(vetor)

    def intercalar_sublistas(self):
        print("\n=== FASE 2: Junção das sublistas ===")
        while len(self.sublistas) > 1:
            novas_sublistas = []
            for i in range(0, len(self.sublistas), 2):
                if i + 1 < len(self.sublistas):
                    sub1 = self.sublistas[i].para_lista()
                    sub2 = self.sublistas[i + 1].para_lista()
                    print(f"-> Junção: {sub1} + {sub2}")
                    time.sleep(self.atraso)
                    intercalada = self._intercalar_duas_listas(sub1, sub2)
                    print(f"-> Resultado: {intercalada}")
                    time.sleep(self.atraso)
                    vetor = Vetor(len(intercalada))
                    for valor in intercalada:
                        vetor.inserir(vetor.tamanho(), valor)
                    novas_sublistas.append(vetor)
                    self.passadas_intercalacao += 1
                else:
                    novas_sublistas.append(self.sublistas[i])
            self.sublistas = novas_sublistas

    def _exibir_resultado(self, resultado, tempo_total):
        print("\n=== RESULTADO FINAL ===")
        print(f"Lista ordenada: {resultado}")
        print(f"Passadas de junção: {self.passadas_intercalacao}")
        print(f"Passadas de Merge Sort: {self.passadas_merge_sort}")
        print(f"Comparações no Merge Sort: {self.comparacoes_merge_sort}")
        print(f"Tempo total: {tempo_total:.2f} segundos")

    def ordenar(self):
        print("=== INICIANDO ORDENAÇÃO EXTERNA ===")
        print(f"Limite de memória: {self.limite_memoria}")
        print(f"Tamanho dos blocos: {self.tamanho_blocos}")
        print(f"Atraso entre passos: {self.atraso} segundos")
        print(f"Tamanho total dos dados: {len(self.dados)}")
        print("=" * 40)

        inicio = time.time()
        self.gerar_sublistas()
        self.intercalar_sublistas()
        resultado_final = self.sublistas[0].para_lista() if self.sublistas else []
        fim = time.time()
        self._exibir_resultado(resultado_final, fim - inicio)
        return resultado_final
