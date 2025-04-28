N, K = input().split()
N, K = int(N), int(K)

arr = input().split()[::-1]

for i in arr[-K:]:
    print(i, end=" ")
