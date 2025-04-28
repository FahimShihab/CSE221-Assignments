def dfs_iterative(root, n, tree):
    subtree_size = [0] * (n + 1)

    stack = [(root, -1)]
    post_order = []
    
    while stack:
        node, parent = stack[-1]

        if subtree_size[node] == 0:
            subtree_size[node] = -1
            post_order.append(node)

            for neighbor in tree[node]:
                if neighbor != parent:
                    stack.append((neighbor, node))
        else:
            stack.pop()
            subtree_size[node] = 1
            for neighbor in tree[node]:
                if neighbor != parent:
                    subtree_size[node] += subtree_size[neighbor]
    
    return subtree_size


def main():
    N, R = map(int, input().split())
    tree = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    subtree_size = dfs_iterative(R, N, tree)

    Q = int(input())
    for _ in range(Q):
        X = int(input())
        print(subtree_size[X])


if __name__ == "__main__":
    main()
