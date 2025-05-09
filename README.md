#  Ordenação Externa Pontuada

## Descrição
Este projeto implementa uma solução de ordenação externa. O algoritmo divide grandes conjuntos de dados em blocos menores que podem ser processados na memória disponível. Esses blocos são ordenados individualmente e, em seguida, combinados para obter o resultado final ordenado.

A abordagem de ordenação externa é especialmente útil quando o conjunto de dados é maior que a memória disponível, exigindo um gerenciamento eficiente dos dados em várias passagens.

## Componentes do Projeto
O projeto consiste em três módulos:

1. **Vetor.py**: Uma classe `Vetor` personalizada usada para representar uma estrutura semelhante a um vetor dinâmico para manipulação dos blocos de dados.
2. **OrdenacaoExterna.py**: O módulo principal que implementa o algoritmo de ordenação externa. Ele lê os dados em blocos, ordena-os usando Merge Sort e intercala os blocos ordenados.
3. **Simulador.py**: Um módulo de simulação que gera dados aleatórios, define parâmetros configuráveis e executa o algoritmo de ordenação externa.

## Como Funciona
### Passo 1: Ordenação dos Blocos (Merge Sort)
Cada bloco de dados é ordenado individualmente usando o algoritmo **Merge Sort**. O Merge Sort é um algoritmo de divisão e conquista que tem uma complexidade de tempo média e no pior caso de **O(n log n)**, onde `n` é o número de elementos no bloco.

### Passo 2: Intercalação dos Blocos Ordenados
Após ordenar os blocos individualmente, o algoritmo intercala-os em pares. Esse processo é semelhante ao Merge Sort aplicado recursivamente, com uma complexidade de **O(n log n)**, onde `n` é o número total de elementos a serem mesclados.

### Passo 3: Resultado Final Ordenado
O processo continua até que todos os blocos tenham sido intercalados em um único conjunto de dados ordenados.

## Parâmetros Configuráveis no terminal de Comando
Você pode ajustar os seguintes parâmetros no modulo `Simulador.py`:
- digita no terminal de comando: python simulador.py <tamanho_dados> [--intervalo_min=N] [--intervalo_max=N] [--limite_memoria=N] [--atraso=F] [--tamanho_blocos=N]

<tamanho_dados>: Obrigatório. O número total de dados a serem gerados. Exemplo: 10.

--intervalo_min=N: Valor mínimo dos dados a serem gerados. O padrão é 1. Exemplo: --intervalo_min=5.

--intervalo_max=N: Valor máximo dos dados a serem gerados. O padrão é 100. Exemplo: --intervalo_max=50.

--limite_memoria=N: Limite de memória disponível para a ordenação. O padrão é 6. Exemplo: --limite_memoria=5.
  
--atraso=F: Opcional. Atraso entre as etapas da simulação, em segundos. O padrão é 0.3. Exemplo: --atraso=0.5.
--tamanho_blocos=N: Tamanho dos blocos lidos em memória durante a simulação. O padrão é 2. Exemplo: --tamanho_blocos=4.
-- (obs: se ao digitar o numero de blocos maior que a memoria, surgirá uma mensagem de erro "memoria nao suportado" automaticamente
o sistema ajustará para o tamanho igual ao da memoria)

Exemplos de Comandos no Terminal:
1) python simulador.py 10 --atraso=0.3
2) python simulador.py 10 --atraso=0.2 --intervalo_min=5

## Complexidade do Algoritmo

### Análise de Complexidade de Tempo
O algoritmo de ordenação externa combina a técnica do Merge Sort para ordenar blocos e a intercalação dessas sublistas. A complexidade de tempo do algoritmo pode ser dividida em duas partes principais: a ordenação dos blocos e a intercalação das sublistas.

1. **Ordenação dos Blocos (Merge Sort)**
   O Merge Sort é usado para ordenar cada bloco individualmente. A complexidade do Merge Sort em um caso genérico é **O(n log n)**, onde `n` é o número de elementos no bloco. Vamos detalhar:

   - **Melhor Caso**: O melhor caso ocorre quando o algoritmo encontra os dados em uma configuração ideal para a ordenação (por exemplo, já parcialmente ordenados). No entanto, como o Merge Sort divide recursivamente a lista em duas metades, o número de comparações e operações será o mesmo. Portanto, o melhor caso também tem complexidade **O(n log n)**.
   
   - **Caso Médio**: No caso médio, o Merge Sort continua com a complexidade **O(n log n)**, independentemente da ordem inicial dos dados. Este é o caso mais comum e representa a complexidade típica do Merge Sort.
   
   - **Pior Caso**: O pior caso também tem complexidade **O(n log n)**, ocorrendo quando os dados estão em uma ordem completamente desfavorável. Mesmo assim, o Merge Sort continua a dividir e intercala as listas de maneira eficiente.

2. **Intercalação das Sublistas**
   Após ordenar os blocos individualmente, o algoritmo realiza a intercalação das sublistas ordenadas. Esse processo é essencialmente o Merge Sort aplicado recursivamente a sublistas menores, o que leva à mesma análise de complexidade **O(n log n)**.

    - **Melhor Caso**: A intercalação pode ser feita rapidamente se as sublistas estiverem quase ordenadas, mas ainda assim o processo de intercalação exige comparar todos os elementos, resultando em complexidade **O(n log n)**.
   
   - **Caso Médio**: O caso médio para intercalação também possui complexidade **O(n log n)**.
   
   - **Pior Caso**: O pior caso para intercalação, onde as sublistas estão em ordens desfavoráveis e precisam ser completamente intercaladas, ainda resulta em **O(n log n)**.

3. **Complexidade Total**
   Como o algoritmo realiza múltiplas passagens para ordenar e intercala as sublistas, a complexidade total depende do número de blocos e da forma como a intercalação é realizada. De forma geral, a complexidade do algoritmo de ordenação externa pode ser expressa como:

   **O(n log n)**, onde `n` é o número total de elementos a serem ordenados.

   Isso inclui tanto a ordenação dos blocos quanto a intercalação das sublistas.

### Complexidade Espacial
O uso de memória adicional para armazenar as sublistas ordenadas e os resultados da intercalação é linear, ou seja, **O(n)**, onde `n` é o número total de elementos a serem ordenados.

Cada bloco de dados é carregado na memória uma vez, e o número de blocos é determinado pelo limite de memória (`LIMITE_MEMORIA`).

## Referências Bibliográficas
- **Algoritmos - Teoria e Prática**, Departamento de Computação, Centro de Ciências Exatas e Tecnologia, Universidade Federal de São Carlos.
- **Algoritmos e Estruturas de Dados em Python**, Departamento de Computação, Centro de Ciências Exatas e Tecnologia, Universidade Federal de São Carlos.

   


 
