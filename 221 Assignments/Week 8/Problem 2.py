def find(u, parent):
    if parent[u] != u:
        parent[u] = find(parent[u], parent)
    return parent[u]

def union(u, v, parent, rank):
    root_u = find(u, parent)
    root_v = find(v, parent)
    if root_u == root_v:
        return False
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    else:
        parent[root_v] = root_u
        if rank[root_u] == rank[root_v]:
            rank[root_u] += 1
    return True

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    # Kruskal's algorithm
    edges.sort()
    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)
    mst_cost = 0

    for w, u, v in edges:
        if union(u, v, parent, rank):
            mst_cost += w

    print(mst_cost)

if __name__ == "__main__":
    main()
