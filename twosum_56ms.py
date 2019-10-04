class Solution(object):
    def twoSum(nums, target):
        if len(nums) < 2: return False
        else:
            buff_dict = {}
            for i in range(len(nums)):
                if nums[i] in buff_dict:
                    return [i,buff_dict[nums[i]]]
                else:
                    buff_dict[target - nums[i]] = i

sol = Solution
print(sol.twoSum(nums = [4,3, 7, 3],target =  11))

