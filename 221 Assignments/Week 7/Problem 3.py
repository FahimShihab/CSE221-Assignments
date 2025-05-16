import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

danger = [float('inf')] * (n + 1)
danger[1] = 0
pq = [(0, 1)]

while pq:
    d, u = heapq.heappop(pq)
    if d > danger[u]:
        continue
    for v, w in graph[u]:
        max_danger = max(d, w)
        if danger[v] > max_danger:
            danger[v] = max_danger
            heapq.heappush(pq, (max_danger, v))

print(' '.join(str(d if d != float('inf') else -1) for d in danger[1:]))
