# Завдання 1

import networkx as nx
import matplotlib.pyplot as plt
from app.banks import bank_names, offshore_bank

# Список укр.банків
bank_names = bank_names()

# Офшорний банк
offshore_bank = offshore_bank()

# Список ребер (транзакції між укр.банками)
edges = []
for i in bank_names:
    for j in bank_names:
        if i != j:
            edges.append((i, j))

# Додавання ребра між останнім банком та офшорним банком
edges.append((bank_names[-1], offshore_bank))

# Створення графа
G = nx.Graph()
G.add_edges_from(edges)

# Визначення позицій вершин для візуалізації графа
pos = nx.circular_layout(G)

# Назва графа
plt.title('Транзакції між укр.банками та офшорним банком')

# Основні характеристики графа
print('Кількість вершин: ', G.number_of_nodes())
print('Кількість ребер: ', G.number_of_edges())
print('Ступінь вершин: ', G.degree())
print('Ступінь центральності вершин: ', nx.degree_centrality(G))
print('Ступінь наближеності вершин: ', nx.closeness_centrality(G))
print('Ступінь посередництва вершин: ', nx.betweenness_centrality(G))

# Візуалізація графа
nx.draw(G, pos, with_labels=True, node_size=1200, font_size=10)

plt.show()
