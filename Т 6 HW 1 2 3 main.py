\Завдання 1 

import networkx as nx
import matplotlib.pyplot as plt
# Створюємо граф, що моделює транспортну мережу міста
graph = nx.Graph()
# Додаємо вершини (перехрестя)
graph.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
# Додаємо ребра (дороги)
graph.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'),
                      ('C', 'F'), ('C', 'G'), ('D', 'H'), ('E', 'I'),
                      ('F', 'J'), ('G', 'J')])
# Візуалізуємо граф
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True)
plt.show()
# Аналіз основних характеристик
print(f"Кількість вершин: {graph.number_of_nodes()}")
print(f"Кількість ребер: {graph.number_of_edges()}")
print("Ступені вершин:")
for node, degree in graph.degree():
    print(f"Вершина {node}: {degree}")




\Завдання 2 

def dfs(graph, start):
    visited = set()
    stack = [start]
    path = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(graph[vertex] - visited)
    return path
def bfs(graph, start):
    visited = set()
    queue = [start]
    path = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            queue.extend(graph[vertex] - visited)
    return path
# Приклад виконання
start_node = 'A'
dfs_path = dfs(graph, start_node)
bfs_path = bfs(graph, start_node)
print(f"Шлях DFS, починаючи з вершини {start_node}: {' -> '.join(dfs_path)}")
print(f"Шлях BFS, починаючи з вершини {start_node}: {' -> '.join(bfs_path)}") 





\Завдання 3 

import heapq
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances
# Приклад виконання
# Додаємо ваги ребер
graph = nx.Graph()
graph.add_weighted_edges_from([('A', 'B', 5), ('A', 'C', 1), ('B', 'D', 2),
                                ('B', 'E', 4), ('C', 'F', 8), ('C', 'G', 3),
                                ('D', 'H', 6), ('E', 'I', 7), ('F', 'J', 2),
                                ('G', 'J', 4)])
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(f"Найкоротші шляхи від вершини {start_node}:")
for node, distance in shortest_paths.items():
    print(f"До вершини {node}: {distance}")





