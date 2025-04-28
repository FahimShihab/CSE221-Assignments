def bfs(start, n, graph):
    visited = []
    parent = []
    for _ in range(n + 1):
        visited.append(False)
        parent.append(-1)

    queue = [start]
    visited[start] = True
    front = 0

    while front < len(queue):
        current = queue[front]
        front += 1
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                queue.append(neighbor)
    
    return parent, visited

def build_path(parent, end):
    path = []
    node = end
    while node != -1:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path

line1 = input()
parts = line1.split()
n = int(parts[0])
m = int(parts[1])
s = int(parts[2])
d = int(parts[3])
k = int(parts[4])

graph = []
for _ in range(n + 1):
    graph.append([])

for _ in range(m):
    edge_line = input()
    edge_parts = edge_line.split()
    u = int(edge_parts[0])
    v = int(edge_parts[1])
    graph[u].append(v)

parent_s, visited_s = bfs(s, n, graph)
parent_k, visited_k = bfs(k, n, graph)

if not visited_s[k] or not visited_k[d]:
    print("-1")
else:
    path1 = build_path(parent_s, k)
    path2 = build_path(parent_k, d)
    full_path = path1 + path2[1:]

    print(len(full_path) - 1)
    for i in range(len(full_path)):
        if i > 0:
            print(" ", end="")
        print(full_path[i], end="")
    print()
