import random
from ordenacao_externa import OrdenacaoExterna  # Importando a classe OrdenacaoExterna

# Definindo os parâmetros
TAMANHO_DADOS = 10
INTERVALO_MIN = 1
INTERVALO_MAX = 100  
LIMITE_MEMORIA = 6
ATRASO = 0.3
TAMANHO_BLOCOS = 7  

if INTERVALO_MAX - INTERVALO_MIN + 1 < TAMANHO_DADOS:
    dados = [random.randint(INTERVALO_MIN, INTERVALO_MAX) for _ in range(TAMANHO_DADOS)]
else:
    dados = random.sample(range(INTERVALO_MIN, INTERVALO_MAX + 1), TAMANHO_DADOS)

print("\n=== EXECUÇÃO DIRETA ===")
print(f"Dados gerados: {dados}")

# Instanciando e executando a ordenação externa
ordenacao = OrdenacaoExterna(dados, LIMITE_MEMORIA, ATRASO, TAMANHO_BLOCOS)
resultado = ordenacao.ordenar()
