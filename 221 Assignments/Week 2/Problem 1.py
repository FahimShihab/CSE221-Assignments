def find_pair(N, S, arr):
    left, right = 0, N - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == S:
            print(left + 1, right + 1)
            return
        elif current_sum < S:
            left += 1
        else:
            right -= 1
    print(-1)

input_values = input().split()
N = int(input_values[0])
S = int(input_values[1])
arr = [int(x) for x in input().split()]
find_pair(N, S, arr)