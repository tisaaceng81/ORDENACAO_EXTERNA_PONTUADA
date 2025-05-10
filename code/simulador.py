import random
import argparse
from ordenacao_externa import OrdenacaoExterna  # Importando a classe OrdenacaoExterna

# Parser de argumentos
parser = argparse.ArgumentParser(description="Simulador de ordenação externa")
parser.add_argument('--tamanho-dados', type=int, required=True, help="Quantidade de dados a serem gerados")
parser.add_argument('--intervalo-min', type=int, default=1, help="Valor mínimo dos dados gerados")
parser.add_argument('--intervalo-max', type=int, default=100, help="Valor máximo dos dados gerados")
parser.add_argument('--limite-memoria', type=int, default=6, help="Limite de memória disponível")
parser.add_argument('--atraso', type=float, default=0.3, help="Atraso entre etapas da simulação")
parser.add_argument('--tamanho-blocos', type=int, default=2, help="Tamanho dos blocos lidos em memória")

args = parser.parse_args()

# Geração dos dados
if args.intervalo_max - args.intervalo_min + 1 < args.tamanho_dados:
    dados = [random.randint(args.intervalo_min, args.intervalo_max) for _ in range(args.tamanho_dados)]
else:
    dados = random.sample(range(args.intervalo_min, args.intervalo_max + 1), args.tamanho_dados)

print("\n=== EXECUÇÃO DIRETA ===")
print(f"Dados gerados: {dados}")

# Instanciando e executando a ordenação externa
ordenacao = OrdenacaoExterna(dados, args.limite_memoria, args.atraso, args.tamanho_blocos)
resultado = ordenacao.ordenar()
