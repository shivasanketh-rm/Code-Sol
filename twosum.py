class Solution(object):
    def twoSum(nums, target):
        for num1 in range(len(nums)):
            for num2 in range(num1+1,len(nums)):
                if  nums[num1] + nums[num2] == target:
                        return [num1, num2]


sol = Solution
print(sol.twoSum(nums = [4,3, 7, 3],target =  11))

