import random
import sys
from ordenacao_externa import OrdenacaoExterna  # Importando a classe OrdenacaoExterna

def exibir_uso():
    print("Uso: python simulador.py <tamanho_dados> [--intervalo_min=N] [--intervalo_max=N] [--limite_memoria=N] [--atraso=F] [--tamanho_blocos=N]")
    print("Parâmetros obrigatórios:")
    print("  <tamanho_dados>         Quantidade de dados a serem gerados (por exemplo, '10')")
    print("Parâmetros opcionais:")
    print("  --intervalo_min=N       Valor mínimo dos dados (padrão = 1)")
    print("  --intervalo_max=N       Valor máximo dos dados (padrão = 100)")
    print("  --limite_memoria=N      Limite de memória (padrão = 6)")
    print("  --atraso=F              Atraso em segundos (padrão = 0.3)")
    print("  --tamanho_blocos=N      Tamanho dos blocos (padrão = 6)")
    sys.exit(1)

# Verifica se ao menos o argumento obrigatório foi passado
if len(sys.argv) < 2:
    exibir_uso()

# O primeiro argumento será o tamanho_dados
try:
    tamanho_dados = int(sys.argv[1])  # O primeiro argumento deve ser o número de dados
except ValueError:
    print("Erro: <tamanho_dados> deve ser um número.")
    exibir_uso()

# Valores padrão para os parâmetros opcionais
intervalo_min = 1
intervalo_max = 100
limite_memoria = 6
atraso = 0.3
tamanho_blocos = 6

# Itera sobre os parâmetros restantes (começando do 2º) para configurar as opções
for i in range(2, len(sys.argv)):
    param = sys.argv[i]
    
    if param.startswith("--"):
        if param.startswith("--intervalo_min="):
            intervalo_min = int(param.split("=")[1])
        elif param.startswith("--intervalo_max="):
            intervalo_max = int(param.split("=")[1])
        elif param.startswith("--limite_memoria="):
            limite_memoria = int(param.split("=")[1])
        elif param.startswith("--atraso="):
            atraso = float(param.split("=")[1])
        elif param.startswith("--tamanho_blocos="):
            tamanho_blocos = int(param.split("=")[1])
        else:
            print(f"Parâmetro desconhecido: {param}")
            exibir_uso()

# Geração dos dados
if intervalo_max - intervalo_min + 1 < tamanho_dados:
    dados = [random.randint(intervalo_min, intervalo_max) for _ in range(tamanho_dados)]
else:
    dados = random.sample(range(intervalo_min, intervalo_max + 1), tamanho_dados)

print("\n=== EXECUÇÃO DIRETA ===")
print(f"Dados gerados: {dados}")

# Instancia e executa a ordenação externa
ordenacao = OrdenacaoExterna(dados, limite_memoria, atraso, tamanho_blocos)
resultado = ordenacao.ordenar()
