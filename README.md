## Descrição do Projeto

Este projeto implementa o algoritmo de multiplicação rápida de Karatsuba em Python. O algoritmo reduz o número de multiplicações necessárias ao dividir os operandos em partes menores e realizar cálculos recursivamente.

### Lógica do Algoritmo
1. Se um dos números for menor que 10, retorna a multiplicação direta.
2. Determina o tamanho do maior número e divide ao meio.
3. Divide os números em partes superiores e inferiores.
4. Calcula os produtos intermediários recursivamente.
5. Combina os resultados para obter o produto final.

## Como Executar o Projeto

### Requisitos
- Python 3.x instalado

### Execução
1. Clone o repositório
   ```sh
   git clone https://github.com/pedrodecampos/trabalho_indiviudal_1_fpaa.git
   cd trabalho_indiviudal-1_fpaa
   ```
2. Execute o script
   ```sh
   python main.py
   ```
3. Insira os números quando solicitado.

## Relatório Técnico

### Complexidade Ciclomática

O fluxo de controle da função `karatsuba` pode ser representado como um grafo com os seguintes elementos:
- Nós (N): representam blocos de código distintos.
- Arestas (E): representam as transições entre blocos.
- Componentes conexos (P): 1 (único programa).

Fórmula: `V(G) = E - N + 2P`

### Complexidade Assintótica

- **Complexidade Temporal**: O algoritmo tem complexidade `O(n^log_2(3))`, aproximadamente `O(n^1.585)`.
- **Complexidade Espacial**: `O(n)`, devido à pilha de recursão.
- **Casos:**
  - Melhor caso: `O(n)` (quando os números são pequenos).
  - Caso médio e pior caso: `O(n^1.585)`, seguindo a decomposição recursiva do problema.
