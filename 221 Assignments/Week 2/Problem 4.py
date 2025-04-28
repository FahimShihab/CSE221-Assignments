def find_first_one(S):
    left, right = 0, len(S) - 1
    first_one = -1
    while left <= right:
        mid = (left + right) // 2
        if S[mid] == '1':
            first_one = mid + 1
            right = mid - 1
        else:
            left = mid + 1
    return first_one

T = int(input())
results = []
for _ in range(T):
    S = input()
    results.append(str(find_first_one(S)))
print("\n".join(results))
