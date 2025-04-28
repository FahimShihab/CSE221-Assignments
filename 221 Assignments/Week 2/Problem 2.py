def merge_sorted_lists(N, alice, M, bob):
    i, j = 0, 0
    merged_list = []
    while i < N and j < M:
        if alice[i] <= bob[j]:
            merged_list.append(alice[i])
            i += 1
        else:
            merged_list.append(bob[j])
            j += 1
    while i < N:
        merged_list.append(alice[i])
        i += 1
    while j < M:
        merged_list.append(bob[j])
        j += 1
    print(" ".join(str(x) for x in merged_list))

N = int(input())
alice = [int(x) for x in input().split()]
M = int(input())
bob = [int(x) for x in input().split()]
merge_sorted_lists(N, alice, M, bob)
