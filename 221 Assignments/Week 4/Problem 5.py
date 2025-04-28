N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split())) 

indegree = [0] * N
outdegree = [0] * N

for i in range(M):
    start = u[i] - 1
    end = v[i] - 1
    
    outdegree[start] += 1
    indegree[end] += 1

result = [indegree[i] - outdegree[i] for i in range(N)]

for value in result:
    print(value, end=" ")
