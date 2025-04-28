def build_balanced_bst(arr):
    result = []
    stack = [(0, len(arr) - 1)]

    while stack:
        left, right = stack.pop()
        if left <= right:
            mid = (left + right) // 2
            result.append(arr[mid])
            stack.append((mid + 1, right))
            stack.append((left, mid - 1))
    
    return result

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    result = build_balanced_bst(A)

    print(*result)

solve()
