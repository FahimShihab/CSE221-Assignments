def path(N, M, u, v):
    adj = [[] for _ in range(N)]
    degree = [0] * N
    
    for i in range(M):
        adj[u[i] - 1].append(v[i] - 1)
        adj[v[i] - 1].append(u[i] - 1)
        degree[u[i] - 1] += 1
        degree[v[i] - 1] += 1
   
    odd_degree_count = sum(1 for d in degree if d % 2 != 0)

    if odd_degree_count != 0 and odd_degree_count != 2:
        return "NO"
    
    visited = [False] * N

    def bfs(start):
        queue = [start]
        visited[start] = True
        while queue:
            node = queue.pop(0)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
    start_node = -1
    for i in range(N):
        if degree[i] > 0:
            start_node = i
            break
    
    if start_node == -1:
        return "NO"
    bfs(start_node)

    for i in range(N):
        if degree[i] > 0 and not visited[i]:
            return "NO"
    
    return "YES"

N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

print(path(N, M, u, v))
