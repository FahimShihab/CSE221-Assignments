import heapq

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: 
            continue
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return dist

n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

alice = dijkstra(n, graph, s)
bob = dijkstra(n, graph, t)

min_time = float('inf')
meeting_node = -1
for i in range(1, n + 1):
    time = max(alice[i], bob[i])
    if time < min_time:
        min_time = time
        meeting_node = i
    elif time == min_time and i < meeting_node:
        meeting_node = i

print(f"{min_time} {meeting_node}" if min_time != float('inf') else -1)
