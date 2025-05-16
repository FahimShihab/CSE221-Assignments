def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent, size):
    root_x = find(x, parent)
    root_y = find(y, parent)
    if root_x != root_y:
        if size[root_x] < size[root_y]:
            root_x, root_y = root_y, root_x
        parent[root_y] = root_x
        size[root_x] += size[root_y]
    return size[find(x, parent)]
def main():
    N, K = map(int, input().split())
    parent = [i for i in range(N + 1)]
    size = [1] * (N + 1)
    
    for _ in range(K):
        a, b = map(int, input().split())
        print(union(a, b, parent, size))

if __name__ == "__main__":
    main()
