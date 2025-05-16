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

def build_mst(n, edges):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    mst_edges = []
    mst_cost = 0

    for w, u, v in sorted(edges):
        if union(u, v, parent, rank):
            mst_edges.append((u, v, w))
            mst_cost += w
            if len(mst_edges) == n - 1:
                break

    if len(mst_edges) < n - 1:
        return None, None
    return mst_cost, mst_edges

from collections import defaultdict, deque

def build_tree_graph(n, mst_edges):
    tree = defaultdict(list)
    for u, v, w in mst_edges:
        tree[u].append((v, w))
        tree[v].append((u, w))
    return tree

def max_edge_on_path(tree, n):

    max_edge = [[0] * (n + 1) for _ in range(n + 1)]
    for start in range(1, n + 1):
        visited = [False] * (n + 1)
        q = deque()
        q.append((start, 0, start))
        visited[start] = True
        while q:
            u, max_w, from_node = q.popleft()
            max_edge[start][u] = max_w
            for v, w in tree[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append((v, max(max_w, w), u))
    return max_edge

def second_best_mst(n, edges):
    mst_cost, mst_edges = build_mst(n, edges)
    if mst_cost is None:
        return -1

    tree = build_tree_graph(n, mst_edges)
    max_edge = max_edge_on_path(tree, n)

    mst_set = set((min(u, v), max(u, v)) for u, v, _ in mst_edges)
    ans = float('inf')

    for w, u, v in edges:
        if (min(u, v), max(u, v)) not in mst_set:
            max_w = max_edge[u][v]
            if max_w < w:
                new_cost = mst_cost - max_w + w
                if new_cost > mst_cost:
                    ans = min(ans, new_cost)

    return ans if ans != float('inf') else -1

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    print(second_best_mst(n, edges))

if __name__ == "__main__":
    main()
