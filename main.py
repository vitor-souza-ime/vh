import networkx as nx
import matplotlib.pyplot as plt

# -----------------------------
# Criando grafo
# -----------------------------
G = nx.les_miserables_graph()

print("\n=== Estatísticas do Grafo ===\n")

print("Número de nós:", G.number_of_nodes())
print("Número de arestas:", G.number_of_edges())

# grau médio
grau_medio = sum(dict(G.degree()).values()) / G.number_of_nodes()
print("Grau médio:", round(grau_medio,2))

# personagem mais conectado
mais_conectado = max(G.degree, key=lambda x: x[1])
print("Personagem mais conectado:", mais_conectado)

# -----------------------------
# Centralidade
# -----------------------------
centralidade = nx.degree_centrality(G)

top5 = sorted(centralidade.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop 5 personagens mais centrais:\n")

for nome, valor in top5:
    print(f"{nome}  ->  {valor:.3f}")

# -----------------------------
# Plotagem do grafo
# -----------------------------
plt.figure(figsize=(12,10))

pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(G, pos,
                       node_size=120,
                       alpha=0.8)

nx.draw_networkx_edges(G, pos,
                       alpha=0.3)

nx.draw_networkx_labels(G, pos,
                        font_size=8)

plt.title("Rede de Personagens — Les Miserables")
plt.axis("off")

plt.show()
