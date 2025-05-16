import heapq

n, m, s, d = map(int, input().split())
weights = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

cost = [float('inf')] * (n + 1)
cost[s] = weights[s - 1]
pq = [(cost[s], s)]

while pq:
    curr_cost, u = heapq.heappop(pq)
    if curr_cost > cost[u]:
        continue
    for v in graph[u]:
        new_cost = curr_cost + weights[v - 1]
        if new_cost < cost[v]:
            cost[v] = new_cost
            heapq.heappush(pq, (new_cost, v))

print(cost[d] if cost[d] != float('inf') else -1)
