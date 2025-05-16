import heapq

n, m, s, d = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

g = [[] for _ in range(n + 1)]
for i in range(m):
    g[u[i]].append((v[i], w[i]))

dist = [float('inf')] * (n + 1)
prev = [-1] * (n + 1)
dist[s] = 0
heap = [(0, s)]

while heap:
    cost, node = heapq.heappop(heap)
    if cost > dist[node]: continue
    for nei, wt in g[node]:
        if dist[nei] > cost + wt:
            dist[nei] = cost + wt
            prev[nei] = node
            heapq.heappush(heap, (dist[nei], nei))

if dist[d] == float('inf'):
    print(-1)
else:
    path = []
    cur = d
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    print(dist[d])
    print(*reversed(path))
