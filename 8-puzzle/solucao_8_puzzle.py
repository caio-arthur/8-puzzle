"""
================================================================================
RELATÓRIO TÉCNICO E ANÁLISE DISCURSIVA - 8-PUZZLE
================================================================================

Autores: 

Caio Arthur Martins de Almeida 
Gustavo Cristelli Santiago
Pedro Henrique Antunes
Gabriel Henrique Silva Oliveira 

Data: 21/08/2025

--------------------------------------------------------------------------------
1. ANÁLISE E DISCUSSÃO (DISCURSIVA)
--------------------------------------------------------------------------------

• Resultados: Qual dos dois algoritmos encontra a solução mais rapidamente 
para um problema simples (poucos movimentos de distância)? E para um problema 
mais complexo?

Para um problema simples, com poucos movimentos até a solução, o BFS (Busca em 
Largura) quase sempre encontrará a solução mais rapidamente. Isso ocorre porque 
o BFS explora o espaço de estados nível por nível. Se a solução está a uma 
profundidade 'd', o BFS a encontrará após explorar todos os caminhos de 
profundidade 'd-1', garantindo o caminho mais curto. O DFS (Busca em 
Profundidade), por outro lado, pode mergulhar em um ramo muito longo e incorreto 
da árvore de busca antes de fazer o backtracking e encontrar o caminho mais 
curto, o que o torna mais lento em "tempo de execução" para soluções rasas.

Para um problema mais complexo (que exige muitos movimentos), a resposta é 
menos direta. O BFS pode se tornar inviável devido ao consumo exponencial de 
memória, pois precisa armazenar todos os nós de cada nível na fila. O DFS, 
embora não garanta o caminho mais curto e possa demorar muito tempo para ser 
executado, consome muito menos memória (proporcional à profundidade máxima da 
busca). Em cenários onde a memória é o fator limitante, o DFS pode ser a única 
opção viável, mesmo que possa levar muito mais tempo para encontrar uma solução 
(que provavelmente não será a ideal). Em termos de "tempo de relógio", o DFS 
pode, por sorte, encontrar uma solução rapidamente se o primeiro caminho que 
explorar profundamente levar ao objetivo. No entanto, em geral, para problemas 
complexos, ambos os algoritmos mostram suas limitações, e algoritmos de busca 
informada como o A* são preferíveis.

• Diferença Fundamental: Explique, com suas próprias palavras, a principal 
diferença entre BFS e DFS em termos de como eles exploram o "espaço de estados" 
do problema. Qual é a principal vantagem de cada um?

A principal diferença reside na estratégia de exploração. Imagine o espaço de 
estados como uma árvore, onde a raiz é o estado inicial.
O BFS explora a árvore de forma "larga e superficial". Ele primeiro visita 
todos os vizinhos diretos da raiz (nível 1), depois todos os vizinhos desses 
nós (nível 2), e assim por diante. É como jogar uma pedra em um lago: as ondas 
se expandem uniformemente em todas as direções. A principal vantagem do BFS é 
que ele sempre garante encontrar o caminho mais curto (com o menor número de 
movimentos) do início ao fim.

O DFS, por sua vez, explora a árvore de forma "profunda e estreita". Ele escolhe 
um caminho e o segue o mais fundo possível até não poder mais avançar. Só então 
ele retrocede (backtracking) e tenta o próximo caminho disponível a partir do 
último ponto de decisão. É como um explorador em um labirinto que sempre vira à 
direita até atingir um beco sem saída, para então voltar e tentar a próxima 
curva. A principal vantagem do DFS é seu baixo consumo de memória, pois ele só 
precisa armazenar o caminho atual que está sendo explorado, em vez de todos os 
nós de uma fronteira inteira.

• Limitações: Para um quebra-cabeça 8x8 (64-puzzle), qual dos dois algoritmos 
falharia mais rapidamente? Por que?

O BFS falharia muito mais rapidamente. O motivo é o consumo de memória, um 
problema conhecido como "explosão combinatória". O número de estados possíveis 
em um 64-puzzle é astronômico. O BFS precisa manter na memória uma fila com 
todos os estados na "fronteira" da busca. O número de nós em cada nível da 
árvore de busca cresce exponencialmente. Para um 64-puzzle, a memória RAM de 
qualquer computador moderno se esgotaria em questão de segundos ou minutos, 
muito antes de chegar perto de uma solução.

O DFS, embora provavelmente nunca encontrasse uma solução em um tempo de vida 
(pois ficaria perdido em caminhos de profundidade imensa), não falharia 
imediatamente por falta de memória. Seu requisito de memória é linear em 
relação à profundidade da busca ($O(d)$), enquanto o do BFS é exponencial em 
relação à profundidade ($O(b^d)$, onde 'b' é o fator de ramificação). Portanto, 
o BFS atinge um limite de recurso físico (memória) de forma muito mais abrupta 
e rápida.

--------------------------------------------------------------------------------
2. RELATÓRIO TÉCNICO SOBRE A ELABORAÇÃO DO CÓDIGO
--------------------------------------------------------------------------------

a) Arquitetura da Solução:
A solução foi dividida em duas partes principais: a lógica de resolução em 
Python e a visualização em HTML/CSS/JavaScript. Optei por uma arquitetura onde o 
script Python é o motor central. Ele executa os algoritmos de busca e, ao final, 
gera um arquivo HTML autônomo. Esta abordagem foi escolhida por sua simplicidade 
e portabilidade: o usuário não precisa de um servidor web ou dependências 
complexas; basta executar o script Python e abrir o arquivo HTML resultante no 
navegador.

b) Implementação em Python:
- Representação de Estado: Conforme solicitado, os estados do tabuleiro são 
  representados como tuplas de 9 elementos. A imutabilidade das tuplas é crucial, 
  pois permite que sejam usadas como chaves em dicionários ou elementos em 
  conjuntos (sets), o que é fundamental para o rastreamento eficiente dos 
  estados já visitados.
  
- Geração de Movimentos: A função `get_possible_moves` é o coração da lógica 
  do puzzle. Ela localiza o espaço em branco (0) e calcula os movimentos 
  válidos (cima, baixo, esquerda, direita) com base em sua posição no grid 3x3, 
  evitando movimentos "fora do tabuleiro".

- Algoritmos de Busca:
  - BFS (Busca em Largura): Utiliza uma `collections.deque`, uma fila otimizada 
    de duas pontas, para gerenciar os estados a serem explorados. A exploração 
    FIFO (First-In, First-Out) garante que a busca se expanda em níveis. Um 
    conjunto `visited` previne ciclos e reprocessamento de estados.
  - DFS (Busca em Profundidade): Utiliza uma lista Python como uma pilha (stack). 
    A exploração LIFO (Last-In, First-Out) faz com que a busca se aprofunde em um 
    caminho antes de explorar outros. O mecanismo de `visited` é igualmente 
    utilizado.
  - Rastreamento do Caminho: Em vez de armazenar apenas o estado na fila/pilha, 
    armazenamos o caminho completo que leva até aquele estado. Isso consome um 
    pouco mais de memória, mas simplifica enormemente a reconstrução do caminho 
    da solução no final, sem a necessidade de ponteiros de "pai" para "filho".

c) Geração da Visualização (HTML/CSS/JS):
- Geração Dinâmica: A função `generate_html_visualization` cria uma string 
  formatada contendo todo o código HTML, CSS e JavaScript. O caminho da solução, 
  calculado em Python, é serializado para o formato JSON usando a biblioteca `json`
  e injetado diretamente no bloco `<script>` do HTML. Isso permite que o JavaScript 
  tenha acesso direto a todos os passos da solução.

- Frontend:
  - HTML: Estrutura semântica simples com um container para o tabuleiro (`#puzzle-board`),
    controles de navegação (botões "Anterior" e "Próximo") e um contador de passos.
  - CSS: Utiliza CSS Grid Layout para criar o tabuleiro 3x3 de forma responsiva 
    e flexível. Estilos simples são aplicados para diferenciar as peças e o espaço 
    vazio, com transições suaves para uma melhor experiência visual.
  - JavaScript: O código JS é responsável pela interatividade. Ele lê o array 
    `solutionPath` (injetado pelo Python), mantém o controle do passo atual e 
    renderiza o tabuleiro correspondente a cada passo. A função `drawBoard` 
    limpa o tabuleiro dinamicamente e recria as peças para cada estado, 
    garantindo uma visualização precisa do movimento.

d) Conclusão:
O código resultante é uma solução completa e autocontida para o problema do 
8-Puzzle, cumprindo todos os requisitos de implementação dos algoritmos de busca 
e fornecendo uma interface de usuário clara e funcional para a análise dos resultados.
A separação entre a lógica de back-end (Python) e a apresentação de front-end 
(HTML/JS) é uma prática de engenharia de software sólida, mesmo em um projeto 
compacto como este.
"""

import collections
import json
import os

# --- LÓGICA DO 8-PUZZLE E ALGORITMOS DE BUSCA ---

def get_possible_moves(state):
    """
    Encontra todos os movimentos possíveis a partir de um estado.
    O estado é uma tupla de 9 elementos. O espaço em branco é 0.
    Retorna uma lista de novos estados (tuplas).
    """
    moves = []
    # Converte para lista para permitir a troca de elementos
    state_list = list(state)
    blank_index = state_list.index(0)

    # Coordenadas (linha, coluna) do espaço em branco
    row, col = divmod(blank_index, 3)

    # Movimento para CIMA
    if row > 0:
        new_state_list = state_list[:]
        swap_index = blank_index - 3
        new_state_list[blank_index], new_state_list[swap_index] = new_state_list[swap_index], new_state_list[blank_index]
        moves.append(tuple(new_state_list))

    # Movimento para BAIXO
    if row < 2:
        new_state_list = state_list[:]
        swap_index = blank_index + 3
        new_state_list[blank_index], new_state_list[swap_index] = new_state_list[swap_index], new_state_list[blank_index]
        moves.append(tuple(new_state_list))

    # Movimento para a ESQUERDA
    if col > 0:
        new_state_list = state_list[:]
        swap_index = blank_index - 1
        new_state_list[blank_index], new_state_list[swap_index] = new_state_list[swap_index], new_state_list[blank_index]
        moves.append(tuple(new_state_list))

    # Movimento para a DIREITA
    if col < 2:
        new_state_list = state_list[:]
        swap_index = blank_index + 1
        new_state_list[blank_index], new_state_list[swap_index] = new_state_list[swap_index], new_state_list[blank_index]
        moves.append(tuple(new_state_list))
    
    return moves

def bfs(initial_state, goal_state):
    """
    Implementação da Busca em Largura (Breadth-First Search).
    Usa uma fila para explorar os estados nível por nível.
    """
    # Fila armazena caminhos completos [ (estado1), (estado2), ... ]
    queue = collections.deque([[initial_state]])
    # Conjunto para rastrear estados já visitados e evitar loops
    visited = {initial_state}

    while queue:
        # Pega o primeiro caminho da fila
        path = queue.popleft()
        current_state = path[-1]

        # Se encontrou a solução, retorna o caminho
        if current_state == goal_state:
            return path
        
        # Gera os próximos movimentos possíveis
        for move in get_possible_moves(current_state):
            if move not in visited:
                visited.add(move)
                # Cria um novo caminho e o adiciona à fila
                new_path = list(path)
                new_path.append(move)
                queue.append(new_path)
    
    # Se a fila esvaziar e não encontrar solução
    return None

def dfs(initial_state, goal_state):
    """
    Implementação da Busca em Profundidade (Depth-First Search).
    Usa uma pilha para explorar os estados o mais fundo possível.
    """
    # Pilha armazena caminhos completos [ (estado1), (estado2), ... ]
    stack = [[initial_state]]
    # Conjunto para rastrear estados já visitados
    visited = {initial_state}

    while stack:
        # Pega o último caminho da pilha
        path = stack.pop()
        current_state = path[-1]

        # Se encontrou a solução, retorna o caminho
        if current_state == goal_state:
            return path
        
        # Gera os próximos movimentos possíveis
        for move in get_possible_moves(current_state):
            if move not in visited:
                visited.add(move)
                # Cria um novo caminho e o adiciona à pilha
                new_path = list(path)
                new_path.append(move)
                stack.append(new_path)
                
    # Se a pilha esvaziar e não encontrar solução
    return None

# --- GERAÇÃO DA VISUALIZAÇÃO EM HTML/CSS/JS ---

def generate_html_visualization(solution_path, algorithm_name):
    """
    Gera um arquivo HTML completo com a visualização da solução.
    """
    # Converte o caminho da solução Python para um array JSON para o JavaScript
    solution_json = json.dumps(solution_path)

    html_content = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visualização do 8-Puzzle</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }}
        h1 {{
            color: #333;
        }}
        #puzzle-board {{
            display: grid;
            grid-template-columns: repeat(3, 100px);
            grid-template-rows: repeat(3, 100px);
            gap: 5px;
            border: 5px solid #333;
            background-color: #666;
            padding: 5px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }}
        .tile {{
            width: 100px;
            height: 100px;
            background-color: #4a90e2;
            color: white;
            font-size: 2.5em;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 4px;
            transition: all 0.2s ease-in-out;
        }}
        .empty {{
            background-color: transparent;
        }}
        #controls {{
            margin-top: 20px;
            display: flex;
            align-items: center;
            gap: 15px;
        }}
        button {{
            padding: 10px 20px;
            font-size: 1em;
            cursor: pointer;
            border: none;
            border-radius: 5px;
            background-color: #333;
            color: white;
        }}
        button:disabled {{
            background-color: #999;
            cursor: not-allowed;
        }}
        #step-info {{
            font-size: 1.2em;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>Solução do 8-Puzzle com {algorithm_name}</h1>
    <div id="puzzle-board"></div>
    <div id="controls">
        <button id="prev-btn">Anterior</button>
        <span id="step-info">Passo: 0 / 0</span>
        <button id="next-btn">Próximo</button>
    </div>

    <script>
        const solutionPath = {solution_json};
        const board = document.getElementById('puzzle-board');
        const prevBtn = document.getElementById('prev-btn');
        const nextBtn = document.getElementById('next-btn');
        const stepInfo = document.getElementById('step-info');

        let currentStep = 0;
        const totalSteps = solutionPath.length - 1;

        function drawBoard(state) {{
            board.innerHTML = ''; // Limpa o tabuleiro anterior
            state.forEach(value => {{
                const tile = document.createElement('div');
                tile.classList.add('tile');
                if (value === 0) {{
                    tile.classList.add('empty');
                }} else {{
                    tile.textContent = value;
                }}
                board.appendChild(tile);
            }});
        }}

        function updateControls() {{
            stepInfo.textContent = `Passo: ${{currentStep}} / ${{totalSteps}}`;
            prevBtn.disabled = currentStep === 0;
            nextBtn.disabled = currentStep === totalSteps;
        }}

        function showStep(step) {{
            if (step >= 0 && step < solutionPath.length) {{
                currentStep = step;
                drawBoard(solutionPath[currentStep]);
                updateControls();
            }}
        }}

        prevBtn.addEventListener('click', () => showStep(currentStep - 1));
        nextBtn.addEventListener('click', () => showStep(currentStep + 1));

        // Inicia a visualização no primeiro passo
        showStep(0);
    </script>
</body>
</html>
    """
    try:
        with open("visualizacao_8_puzzle.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        return True
    except IOError as e:
        print(f"Erro ao escrever o arquivo HTML: {e}")
        return False

# --- BLOCO PRINCIPAL DE EXECUÇÃO ---

if __name__ == "__main__":
    # Estado inicial (exemplo que tem solução)
    initial_state = (1, 2, 3, 4, 8, 0, 7, 6, 5) 
    
    # Estado objetivo
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    print("=========================================")
    print("      Solucionador do 8-Puzzle      ")
    print("=========================================")
    print(f"Estado Inicial: {initial_state}")
    print(f"Estado Objetivo: {goal_state}")
    print("\nEscolha o algoritmo de busca:")
    print("1. Busca em Largura (BFS)")
    print("2. Busca em Profundidade (DFS)")

    choice = ""
    while choice not in ["1", "2"]:
        choice = input("Digite sua escolha (1 ou 2): ")

    if choice == "1":
        print("\nExecutando Busca em Largura (BFS)...")
        solution_path = bfs(initial_state, goal_state)
        algorithm_name = "BFS"
    else:
        print("\nExecutando Busca em Profundidade (DFS)...")
        solution_path = dfs(initial_state, goal_state)
        algorithm_name = "DFS"

    if solution_path:
        print(f"\nSolução encontrada em {len(solution_path) - 1} movimentos!")
        # Descomente a linha abaixo para ver todos os passos no console
        # for i, state in enumerate(solution_path):
        #     print(f"Passo {i}: {state}")
        
        print("\nGerando arquivo de visualização...")
        if generate_html_visualization(solution_path, algorithm_name):
            # Tenta abrir o arquivo automaticamente no navegador
            filepath = os.path.abspath("visualizacao_8_puzzle.html")
            print(f"Arquivo 'visualizacao_8_puzzle.html' criado com sucesso!")
            print(f"Abra este arquivo em seu navegador para ver a solução passo a passo.")
            print(f"Caminho: file://{filepath}")
            
    else:
        print("\nNão foi possível encontrar uma solução.")