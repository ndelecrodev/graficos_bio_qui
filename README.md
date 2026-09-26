# Gráficos de crescimento celular

Projeto educacional em Python para visualizar a relação entre o tempo de observação e a quantidade de células em um experimento. O programa gera dois gráficos com os mesmos dados: um em escala linear e outro usando o logaritmo de base 10 da quantidade de células.

## Objetivo

O projeto auxilia a observar como uma população celular cresce ao longo do tempo e como a transformação logarítmica pode facilitar a análise de variações que abrangem ordens de grandeza diferentes.

Os dados usados atualmente são:

| Tempo (h) | Células |
| ---: | ---: |
| 4 | 1.000 |
| 8 | 5.000 |
| 12 | 10.000 |
| 16 | 20.000 |
| 20 | 35.000 |
| 24 | 65.000 |

## Tecnologias

- Python 3.14 ou superior
- [Matplotlib](https://matplotlib.org/)
- [Poetry](https://python-poetry.org/) para gerenciamento do ambiente e das dependências

## Pré-requisitos

Instale o Python 3.14 ou uma versão compatível com `pyproject.toml` e o Poetry. Depois, clone o repositório e entre na pasta do projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd graficos_multi
```

## Instalação

Instale as dependências declaradas no projeto:

```bash
poetry install
```

O comando cria ou utiliza o ambiente virtual do Poetry e instala o Matplotlib. O grupo de desenvolvimento também inclui o Pytest para eventuais testes.

## Execução

Execute o programa com:

```bash
poetry run python main.py
```

O script abre uma janela com os gráficos gerados. É necessário executar em um ambiente com suporte à exibição de janelas gráficas.

## Gráficos gerados

1. **Graph Etapa 3**: apresenta a quantidade de células em escala linear em função do tempo.
2. **Graph Etapa 4**: apresenta `log10(células)` em função do tempo, permitindo comparar melhor os valores quando a escala dos dados varia bastante.

Os dois gráficos usam marcadores nos pontos medidos, grade e os rótulos definidos em `main.py`.

## Estrutura do projeto

```text
graficos_multi/
├── graphs/
│   └── graph.py       # Funções para criar e exibir gráficos
├── tools/
│   └── tool.py        # Cálculo do logaritmo de base 10
├── main.py            # Dados do experimento e ponto de entrada
├── pyproject.toml     # Configuração do Poetry e dependências
└── poetry.lock        # Versões resolvidas das dependências
```

### Componentes principais

- `main.py` define os tempos, as quantidades de células e solicita a criação dos dois gráficos.
- `graphs.graph.Graph.build_graph` configura cada gráfico com título, eixos, marcadores e grade.
- `graphs.graph.Graph.plotar` exibe as figuras na tela.
- `tools.tool.Tool.calcular_logs` calcula o logaritmo decimal de cada valor da lista.

## Observações e limitações

- A execução atual usa dados definidos diretamente em `main.py`; não há leitura de arquivos externos nem interface para entrada de novos dados.
- O gráfico logarítmico requer valores positivos, pois `log10` não é definido para zero ou números negativos. Atualmente, `Tool.calcular_logs` retorna `0` quando a lista contém zero, em vez de retornar uma lista transformada; novos dados devem ser validados antes de serem usados.
- O projeto é voltado à visualização didática. Os gráficos não realizam ajuste de curva, cálculo de taxa de crescimento ou análise estatística.

## Licença

O projeto não declara uma licença de uso no momento (`license = "no license"` no `pyproject.toml`).
