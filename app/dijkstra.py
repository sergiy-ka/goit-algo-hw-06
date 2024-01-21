# Алгоритм Дейкстри

def dijkstra(graph, start):
    # Ініціалізація вартостей та попередників
    inf = float('inf')
    costs = {node: inf for node in graph.nodes}
    costs[start] = 0
    predecessors = {node: None for node in graph.nodes}

    # Множина відвіданих вершин
    visited = set()

    # Основний цикл
    while len(visited) < len(graph.nodes):
        # Вибір вершини з найменшою вартістю
        current_node = min(
            (node for node in costs if node not in visited), key=lambda node: costs[node]
        )

        # Оновлення вартостей та попередників для сусідніх вершин
        for neighbor in graph.neighbors(current_node):
            new_cost = costs[current_node] + \
                graph[current_node][neighbor]['weight']
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                predecessors[neighbor] = current_node

        # Додаємо поточну вершину до відвіданих
        visited.add(current_node)

    return costs, predecessors
