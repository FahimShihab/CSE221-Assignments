def longest_subarray(N, K, arr):
    left = 0
    current_sum = 0
    max_length = 0
    for right in range(N):
        current_sum += arr[right]
        
        while current_sum > K:
            current_sum -= arr[left]
            left += 1
        max_length = max(max_length, right - left + 1)
    print(max_length)

input_values = input().split()
N = int(input_values[0])
K = int(input_values[1])
arr = [int(x) for x in input().split()]
longest_subarray(N, K, arr)
