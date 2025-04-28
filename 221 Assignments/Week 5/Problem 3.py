def bfs_lex_smallest_path(n, m, s, d, u_list, v_list):
    graph = []
    for _ in range(n + 1):
        graph.append([])

    for i in range(m):
        u = int(u_list[i])
        v = int(v_list[i])
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n + 1):
        graph[i].sort()

    visited = []
    parent = []
    for _ in range(n + 1):
        visited.append(False)
        parent.append(-1)

    queue = [s]
    visited[s] = True

    found = False
    front = 0
    while front < len(queue):
        current = queue[front]
        front += 1
        if current == d:
            found = True
            break
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                queue.append(neighbor)

    if not found:
        print("-1")
        return

    path = []
    node = d
    while node != -1:
        path.append(node)
        node = parent[node]
    path.reverse()

    print(len(path) - 1)
    for i in range(len(path)):
        if i > 0:
            print(" ", end="")
        print(path[i], end="")
    print()

line1 = input()
parts = line1.split()
n = int(parts[0])
m = int(parts[1])
s = int(parts[2])
d = int(parts[3])

u_line = input()
u_list = u_line.split()

v_line = input()
v_list = v_line.split()

bfs_lex_smallest_path(n, m, s, d, u_list, v_list)
