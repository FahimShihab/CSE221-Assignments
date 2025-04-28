a = input()
b = a.split()
N = int(b[0])
M = int(b[1])

adj_matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(0)
    adj_matrix.append(row)

for _ in range(M):
    edge_input = input().split()
    u = int(edge_input[0])
    v = int(edge_input[1])
    w = int(edge_input[2])
    adj_matrix[u-1][v-1] = w

for i in range(N):
    for j in range(N):
        print(adj_matrix[i][j], end=' ')
    print()
