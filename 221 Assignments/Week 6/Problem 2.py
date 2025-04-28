def max_robots_or_humans(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        u = edges[i][0]
        v = edges[i][1]
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    color = [0] * (n + 1)
    result = 0

    for i in range(1, n + 1):
        if not visited[i]:
            queue = [i]
            visited[i] = True
            color[i] = 0
            count0 = 1
            count1 = 0
            head = 0

            is_bipartite = True

            while head < len(queue):
                node = queue[head]
                head += 1
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        color[neighbor] = 1 - color[node]
                        if color[neighbor] == 0:
                            count0 += 1
                        else:
                            count1 += 1
                        queue.append(neighbor)
                    else:
                        if color[neighbor] == color[node]:
                            is_bipartite = False

            if not is_bipartite:
                return 0
            if count0 > count1:
                result += count0
            else:
                result += count1

    return result

first = input().split()
n = int(first[0])
m = int(first[1])
edges = []
for _ in range(m):
    u_v = input().split()
    u = int(u_v[0])
    v = int(u_v[1])
    edges.append([u, v])

print(max_robots_or_humans(n, m, edges))
