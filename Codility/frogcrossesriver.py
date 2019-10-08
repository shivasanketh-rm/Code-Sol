def solution(A, x):
    y = list(range(1,x+1))
    print(y)
    for i in range(len(A)):
        if A[i] in y:
            y.remove(A[i])
            if y == []:
                return i
    


print(solution([1,3,1,4,2,3,5,4],5))