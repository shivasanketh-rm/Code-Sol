class Solution:
    def lengthOfLongestSubstring(s):
        max_length = 0
        for i in range(len(s)):
            arr = []
            for k in range(i,len(s)):
                if (s[k] in arr):
                    break
                else:
                    arr.append(s[k])

            length = len(arr)
            max_length = max(max_length, length)
                
            
        return max_length

sol = Solution
print("Length of longest Substring = {}" .format(sol.lengthOfLongestSubstring("abcdbcdefa")))

class Solution2:
    def lengthOfLongestSubstring(s):
        max_length = 0
        for i,j in enumerate(s):
            arr = []
            for k in range(i,len(s)):
                print("len(s)-1 = ", len(s)-1)
                if (s[k] in arr):
                    break
                else:
                    arr.append(s[k])

            length = len(arr)
            print(i, j, arr, length)
            max_length = max(max_length, length)
        return max_length





