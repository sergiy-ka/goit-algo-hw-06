# Завдання 3

import networkx as nx
import matplotlib.pyplot as plt
from app.banks import bank_names, offshore_bank, bank_trn_cost
from app.dijkstra import dijkstra

# Список укр.банків
bank_names = bank_names()

# Офшорний банк
offshore_bank = offshore_bank()

# Список ребер (транзакції між банками)
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

# Задання ваг ребер (вартість транзакцій переказу між банками)
for (u, v) in G.edges():
    G[u][v]['weight'] = bank_trn_cost(u, v)

# Визначення позицій вершин для візуалізації графа
pos = nx.circular_layout(G)

# Назва графа
plt.title('Вартість транзакцій між укр.банками та офшорним банком')

# Пошук найдешевшого шляху для переказу коштів в офшорний банк
start_bank = bank_names[0]
costs, predecessors = dijkstra(G, start_bank)

# Виведення результатів
print("\nВибір найдешевшого шляху:")
for target_bank, cost in costs.items():
    path = [target_bank]
    while predecessors[target_bank] is not None:
        target_bank = predecessors[target_bank]
        path.insert(0, target_bank)
    print(f"Від {start_bank} до {path[-1]}: {cost} одиниць, Шлях: {path}")

print(f"""\nНайдешевший шлях для переказу коштів з банку {start_bank} в офшорний банк {offshore_bank}: {path}
Вартість: {costs[offshore_bank]} одиниць""")

# Візуалізація графа
nx.draw(G, pos, with_labels=True, node_size=1200, font_size=10)

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Виділити зеленим кольором найдешевший шлях для переказу коштів в офшорний банк
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='g')
nx.draw_networkx_edges(G, pos, edgelist=[(
    path[i], path[i+1]) for i in range(len(path)-1)], edge_color='g', width=1)

plt.show()
