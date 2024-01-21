# Завдання 2

from collections import deque
from app.dfs import dfs_recursive
from app.bfs import bfs_recursive
from app.banks import bank_names, offshore_bank

# Список укр.банків
bank_names = bank_names()

# Офшорний банк
offshore_bank = offshore_bank()

# Представлення графа за допомогою списку суміжності
graph = {}
for i in bank_names:
    graph[i] = []
    for j in bank_names:
        if i != j:
            graph[i].append(j)

# Додавання офшорного банка до графа
graph[offshore_bank] = [bank_names[-1]]

# Додавання ребра між останнім банком та офшорним банком
graph[bank_names[-1]].append(offshore_bank)

if __name__ == '__main__':

    print(f"""\nПредставлення графа за допомогою списку суміжності: 
{graph}""")

    # Порівняння результатів пошуку шляхів в графі за допомогою алгоритмів DFS і BFS
    print('\nРезультати пошуку шляхів в графі за допомогою алгоритму DFS:')
    dfs_recursive(graph, bank_names[0])

    print('\n\nРезультати пошуку шляхів в графі за допомогою алгоритму BFS:')
    bfs_recursive(graph, deque([bank_names[0]]))

    # Пояснення різниці в отриманих шляхах
    print('\n\nВисновки щодо різниці в отриманих шляхах:')
    print("""З результатів пошуку шляхів в графі бачимо, що різні алгоритми обходу графу можуть виводити різні послідовності вершин. 
DFS крокує глибше, обираючи один шлях, тоді як BFS розглядає всі можливі шляхи на одному рівні перед переходом до наступного рівня.""")
