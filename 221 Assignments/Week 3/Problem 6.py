def build_postorder(in_start, in_end, pre_index):
    if in_start > in_end:
        return []
    root = preorder[pre_index[0]]
    pre_index[0] += 1
    root_index = in_order_map[root]
    left_subtree = build_postorder(in_start, root_index - 1, pre_index)
    right_subtree = build_postorder(root_index + 1, in_end, pre_index)

    return left_subtree + right_subtree + [root]

def solve():
    N = int(input().strip())
    in_order = list(map(int, input().split()))
    
    global preorder
    preorder = list(map(int, input().split()))

    global in_order_map
    in_order_map = {}
    for index, value in enumerate(in_order):
        in_order_map[value] = index
    pre_index = [0]
    post_order = build_postorder(0, N - 1, pre_index)

    print(" ".join(str(x) for x in post_order))

solve()
