import heapq

n, m, s, d = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

INF = float('inf')
dist1 = [INF] * (n + 1)
dist2 = [INF] * (n + 1)

pq = [(0, s)]
dist1[s] = 0

while pq:
    cost, node = heapq.heappop(pq)

    for neighbor, weight in graph[node]:
        new_cost = cost + weight

        if new_cost < dist1[neighbor]:
            dist2[neighbor] = dist1[neighbor]
            dist1[neighbor] = new_cost
            heapq.heappush(pq, (new_cost, neighbor))

        elif dist1[neighbor] < new_cost < dist2[neighbor]:
            dist2[neighbor] = new_cost
            heapq.heappush(pq, (new_cost, neighbor))

print(dist2[d] if dist2[d] != INF else -1)
