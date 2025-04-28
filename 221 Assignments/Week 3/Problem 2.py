def max_value(A, left, right):
    if right - left == 1:  # Base case: only two elements
        return A[left] + A[right] ** 2
    
    mid = (left + right) // 2
    
    # Recursively find the maximum in the left and right halves
    max_left = max_value(A, left, mid)
    max_right = max_value(A, mid, right)
    
    # Find the maximum A[i] from the left half
    max_Ai_left = max(A[left:mid])
    
    # Find the maximum A[j] from the right half
    max_Aj_right = max(A[mid:right])
    
    # Calculate the maximum value using the best Ai from the left and Aj from the right
    cross_max = max_Ai_left + (max_Aj_right ** 2)
    
    # Return the maximum of the three computed values
    return max(max_left, max_right, cross_max)

def main():
    N = int(input("Enter the number of elements (N): "))
    A = list(map(int, input("Enter the elements separated by spaces: ").split()))
    
    result = max_value(A, 0, N-1)
    print("The maximum value of A[i] + (A[j])^2 is:", result)

if __name__ == "__main__":
    main()