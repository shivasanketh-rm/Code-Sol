class Solution:
    def repeatedNTimes(A):
        for a in range(len(A)):
            if A[a] in A[:a]:
                return A[a]

sol = Solution
print("Container with most water = {}" .format(sol.repeatedNTimes([5,4,3,3])))