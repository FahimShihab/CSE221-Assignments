def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    N_Q = input().split()
    N = int(N_Q[0])
    Q = int(N_Q[1])

    coprime_neighbors = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j and gcd(i, j) == 1:
                coprime_neighbors[i].append(j)
        coprime_neighbors[i].sort()

    for _ in range(Q):
        x_k = input().split()
        X = int(x_k[0])
        K = int(x_k[1])
        neighbors = coprime_neighbors[X]
        if K <= len(neighbors):
            print(neighbors[K - 1])
        else:
            print(-1)

main()
