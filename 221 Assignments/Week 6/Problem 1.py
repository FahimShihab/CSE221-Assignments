import heapq

def find_course_order(n, m, prereq):
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for i in range(m):
        a = prereq[i][0]
        b = prereq[i][1]
        graph[a].append(b)
        in_degree[b] += 1

    heap = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heapq.heappush(heap, i)

    order = []
    while heap:
        current = heapq.heappop(heap)
        order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(heap, neighbor)

    if len(order) != n:
        print(-1)
    else:
        for i in range(len(order)):
            print(order[i], end=' ')
        print()

first = input().split()
n = int(first[0])
m = int(first[1])

prereq = []
for _ in range(m):
    pair = input().split()
    a = int(pair[0])
    b = int(pair[1])
    prereq.append([a, b])

find_course_order(n, m, prereq)
