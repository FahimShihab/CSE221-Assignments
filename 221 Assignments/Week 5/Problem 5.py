line1 = input()
parts = line1.split()
n = int(parts[0])
m = int(parts[1])

graph = []
color = []

for _ in range(n + 1):
    graph.append([])
    color.append(0)

for _ in range(m):
    u, v = input().split()
    u = int(u)
    v = int(v)
    graph[u].append(v)

def cycle_iteration(start):
    stack = [(start, 0)]
    path = []

    while stack:
        node, i = stack[-1]

        if color[node] == 0:
            color[node] = 1
            path.append(node)

        neighbors = graph[node]
        if i < len(neighbors):
            neighbor = neighbors[i]
            stack[-1] = (node, i + 1)

            if color[neighbor] == 0:
                stack.append((neighbor, 0))
            elif color[neighbor] == 1:
                return True
        else:
            color[node] = 2
            stack.pop()
            path.pop()

    return False

found = False
for i in range(1, n + 1):
    if color[i] == 0:
        if cycle_iteration(i):
            found = True
            break

if found:
    print("YES")
else:
    print("NO")
