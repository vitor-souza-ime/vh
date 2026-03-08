# Análise de Rede — Les Misérables

Este projeto implementa a **análise de rede de coocorrência de personagens** do romance *Les Misérables* de Victor Hugo, utilizando o dataset de rede fornecido pelo NetworkX.

## Funcionalidades

- Criação do grafo de personagens com **NetworkX**
- Estatísticas do grafo impressas na **CLI**:
  - Número de nós e arestas
  - Grau médio
  - Personagem mais conectado
  - Top 5 personagens mais centrais
- Visualização do grafo com **Matplotlib**, destacando conexões entre personagens

## Requisitos

- Python 3.8+
- Bibliotecas:
  - networkx
  - matplotlib

Instalação rápida:

```bash
pip install networkx matplotlib
````

## Estrutura do projeto

```text
vh/
├── main.py       # Código principal para análise da rede
└── README.md     # Este arquivo
```

## Execução

Para executar o script e gerar as estatísticas e o gráfico:

```bash
python main.py
```

O script exibirá informações na CLI sobre o grafo e abrirá uma janela com o gráfico da rede.

## Referências

* NetworkX — [https://networkx.org](https://networkx.org)
* Les Misérables Graph Dataset — fornecido pelo NetworkX

## Licença

MIT License

