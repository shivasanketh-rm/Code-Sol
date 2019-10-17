def diagonalDifference(arr):
    # Write your code here
    return arr
    sum_a = 0
    sum_b = 0
    for i in range(len(arr)):
        sum_a = sum_a + arr[i][i]
        sum_b = sum_b + arr[len(arr)-i-1][i] 
    return abs(sum_a - sum_b)

print("a")
print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))