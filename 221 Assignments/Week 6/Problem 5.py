from collections import deque

def bfs(start, n, tree):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    
    farthest_node = start
    max_dist = 0
    
    while q:
        node = q.popleft()
        for neighbor in tree[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
                if dist[neighbor] > max_dist:
                    max_dist = dist[neighbor]
                    farthest_node = neighbor
                    
    return farthest_node, max_dist, dist

def main():
    N = int(input())
    tree = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    arbitrary_node = 1
    node_A, _, _ = bfs(arbitrary_node, N, tree)

    node_B, max_distance, _ = bfs(node_A, N, tree)

    print(max_distance)
    print(node_A, node_B)

if __name__ == "__main__":
    main()
