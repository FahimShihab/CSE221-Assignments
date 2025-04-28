def selection_sort_with_swaps(stu):
    n = len(stu)
    swap_count = 0

    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if (stu[j][1] > stu[max_idx][1]) or \
               (stu[j][1] == stu[max_idx][1] and stu[j][0] < stu[max_idx][0]):
                max_idx = j

        if max_idx != i:
            stu[i], stu[max_idx] = stu[max_idx], stu[i]
            swap_count += 1

    return swap_count, stu


N = int(input())
IDs = list(map(int, input().split()))
Marks = list(map(int, input().split()))

stu = list(zip(IDs, Marks))

swap_count, sorted_stu = selection_sort_with_swaps(stu)

print(f"Minimum swaps: {swap_count}")
for sid, mark in sorted_stu:
    print(f"ID: {sid} Mark: {mark}")
