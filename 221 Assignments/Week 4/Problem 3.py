a = input()
N = int(a)

adj_matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(0)
    adj_matrix.append(row)

for i in range(N):
    a = input().split()
    k = int(a[0])
    for j in range(1, k + 1):
        neighbor = int(a[j])
        adj_matrix[i][neighbor] = 1

for i in range(N):
    for j in range(N):
        print(adj_matrix[i][j], end=' ')
    print()
