def bfs_traversal(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    for u in range(1, n + 1):
        graph[u].sort()

    visited = [False] * (n + 1)
    queue = [1]
    visited[1] = True
    result = []

    front = 0
    while front < len(queue):
        u = queue[front]
        front += 1
        result.append(u)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    print(" ".join(str(x) for x in result))

n_m = input().split()
n = int(n_m[0])
m = int(n_m[1])
edges = []

for _ in range(m):
    u_v = input().split()
    u = int(u_v[0])
    v = int(u_v[1])
    edges.append((u, v))

bfs_traversal(n, m, edges)
