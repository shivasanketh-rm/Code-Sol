class Solution:
    def lengthOfLongestSubstring(s):
        substring = ''
        max_length = 0
        for c in s:
            if c not in substring:
                substring += c
            else:
                substring = substring[substring.index(c) + 1:] + c
            #5 check max length between current max with new length of seen
            max_length = max(max_length, len(substring))
        return max_length

sol = Solution
print("Length of longest Substring = {}" .format(sol.lengthOfLongestSubstring("abcdbcdefa")))






