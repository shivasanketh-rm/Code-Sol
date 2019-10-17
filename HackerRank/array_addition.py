def aVeryBigSum(ar):
    sum = 0
    print(ar)
    for i in range(ar[0]):
        sum = sum + ar[1][i]
        #print(sum)
    return sum

print("a")
print(aVeryBigSum([5,[1000000001, 1000000002, 1000000001, 1000000001, 1000000001]]))