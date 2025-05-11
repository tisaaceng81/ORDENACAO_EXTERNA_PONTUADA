import random
import sys
from ordenacao_externa import OrdenacaoExterna  # Importa a classe de ordenação externa

def exibir_ajuda():
    print("Uso: python simulador.py <quantidade_dados> [--valor_minimo=N] [--valor_maximo=N] [--limite_memoria=N] [--atraso=F] [--tamanho_blocos=N]")
    print("Parâmetros obrigatórios:")
    print("  <quantidade_dados>       Quantidade de dados a serem gerados (exemplo: '10')")
    print("Parâmetros outros:")
    print("  --valor_minimo=N         Valor mínimo dos dados (padrão = 1)")
    print("  --valor_maximo=N         Valor máximo dos dados (padrão = 100)")
    print("  --limite_memoria=N       Limite da memória disponível (padrão = 6)")
    print("  --atraso=F               Atraso entre operações, em segundos (padrão = 0.3)")
    print("  --tamanho_blocos=N       Tamanho dos blocos de dados (padrão = 6)")

# Valores padrão
quantidade_dados = 10
valor_minimo = 1
valor_maximo = 100
limite_memoria = 6
atraso = 0.3
tamanho_blocos = 6

# Se argumentos foram fornecidos, tenta usar o primeiro como quantidade de dados
if len(sys.argv) >= 2:
    try:
        quantidade_dados = int(sys.argv[1])
    except ValueError:
        print("Erro: <quantidade_dados> deve ser um número inteiro.")
        exibir_ajuda()
        sys.exit(1)  # Sai se houver erro

# Lê os demais parâmetros outros
for i in range(2, len(sys.argv)):
    parametro = sys.argv[i]
    
    if parametro.startswith("--"):
        if parametro.startswith("--valor_minimo="):
            valor_minimo = int(parametro.split("=")[1])
        elif parametro.startswith("--valor_maximo="):
            valor_maximo = int(parametro.split("=")[1])
        elif parametro.startswith("--limite_memoria="):
            limite_memoria = int(parametro.split("=")[1])
        elif parametro.startswith("--atraso="):
            atraso = float(parametro.split("=")[1])
        elif parametro.startswith("--tamanho_blocos="):
            tamanho_blocos = int(parametro.split("=")[1])
        else:
            print(f"Parâmetro desconhecido: {parametro}")
            exibir_ajuda()
            sys.exit(1)  # Sai se houver erro

# Geração dos dados aleatórios
if valor_maximo - valor_minimo + 1 < quantidade_dados:
    dados = [random.randint(valor_minimo, valor_maximo) for _ in range(quantidade_dados)]
else:
    dados = random.sample(range(valor_minimo, valor_maximo + 1), quantidade_dados)

print("\n=== INÍCIO DA EXECUÇÃO ===")
print(f"Dados gerados: {dados}")

# Criação e execução da ordenação externa
ordenador = OrdenacaoExterna(dados, limite_memoria, atraso, tamanho_blocos)
resultado = ordenador.ordenar()
