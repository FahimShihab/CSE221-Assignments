def binary_search_count(arr, x, y):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    left_index = left  

    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= y:
            left = mid + 1
        else:
            right = mid
    right_index = left  
    return right_index - left_index  

nq = input().split()
n = int(nq[0])
q = int(nq[1])

arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])

for _ in range(q):
    xy = input().split()
    x = int(xy[0])
    y = int(xy[1])
    print(binary_search_count(arr, x, y))
