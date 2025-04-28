def dfs_iteration(n, m, u_list, v_list):
    graph = []
    for _ in range(n + 1):
        graph.append([])

    for i in range(m):
        u = int(u_list[i])
        v = int(v_list[i])
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n + 1):
        graph[i].sort(reverse=True)

    visited = []
    for _ in range(n + 1):
        visited.append(False)

    stack = [1]
    result = []

    while len(stack) > 0:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            result.append(u)
            for i in range(len(graph[u])):
                v = graph[u][i]
                if not visited[v]:
                    stack.append(v)

    for i in range(len(result)):
        if i > 0:
            print(" ", end="")
        print(result[i], end="")
    print()

line = input()
parts = line.split()
n = int(parts[0])
m = int(parts[1])

u_line = input()
u_list = u_line.split()

v_line = input()
v_list = v_line.split()

dfs_iteration(n, m, u_list, v_list)
