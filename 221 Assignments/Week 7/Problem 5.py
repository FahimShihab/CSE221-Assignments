import heapq

n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for i in range(m):
    graph[u[i]].append((v[i], w[i]))

INF = float('inf')
dist = [[INF, INF] for _ in range(n + 1)]
pq = []

for nei, wei in graph[1]:
    parity = wei % 2
    dist[nei][parity] = wei
    heapq.heappush(pq, (wei, nei, parity))

while pq:
    cost, node, last_parity = heapq.heappop(pq)
    if dist[node][last_parity] < cost:
        continue
    for nei, wei in graph[node]:
        curr_parity = wei % 2
        if curr_parity == last_parity:
            continue
        new_cost = cost + wei
        if new_cost < dist[nei][curr_parity]:
            dist[nei][curr_parity] = new_cost
            heapq.heappush(pq, (new_cost, nei, curr_parity))

ans = min(dist[n])
print(ans if ans != INF else -1)
