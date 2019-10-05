import math


class Solution( object):
    def longestPalindrome(self, s):
        max_string = ''
        for i in range(len(s)):
            for j in range(i+len(max_string),len(s)+1):
                if self.checkpalindrome(s[i:j]):
                        max_string = s[i:j]


        return max_string

    def checkpalindrome(self, Substring):
        #print("string received in checkPalindrome = ", Substring)
        return Substring==Substring[::-1]

    


sol = Solution()
print("Length of longest Palindromic Substring = {}" .format(sol.longestPalindrome(s = "baabaaaab")))


class Solution2( object):
    def longestPalindromicSubstring(self, s):
        max_string = ''
        max_length = 0
        for i in range(len(s)):
            print("i = {}, s[i] = {}" .format(i,s[i]))
            for j in range(i+1,len(s)+1):
                #print("j = ", j)
                check_palindrome = self.checkpalindrome(s[i:j])
                #print("i = {}, j = {},s[i:j] = {}" .format(i,j,s[i:j]))
                if check_palindrome:
                    #print("inside check palindrome")
                    if max_length < len(s[i:j]):
                        max_length = len(s[i:j])
                        max_string = s[i:j]


        return max_string

    def checkpalindrome(self, Substring):
        #print("string received in checkPalindrome = ", Substring)
        for i in range(math.ceil(len(Substring)/2)):
            if Substring[i] != Substring[-1-i]:
                return False

        return True