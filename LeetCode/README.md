# Linked_list_addition.py
*You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.*

*You may assume the two numbers do not contain any leading zero, except the number 0 itself.*

**Code:**
Definition for singly-linked list.

    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    class Solution:
        def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            temp = cur = ListNode(0)
            carry = 0

            while l1 or l2 or carry:
                if l1:
                    carry += l1.val
                    l1 = l1.next
                if l2:
                    carry += l2.val
                    l2 = l2.next
                #print("carry = ", carry)
                #print("carry%10 = ",carry%10)
                temp.next = ListNode(carry % 10)
                temp = temp.next
                carry = carry // 10
                #print("carry // 10 = ",carry // 10 )
            return cur.next
        
---------------------------------------------------------------------------------------------------------------

# lengthOfLongestSubstring

*Given a string, find the length of the longest substring without repeating characters. * 
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        max_length = 0
        for c in s:
            if c not in substring:
                substring += c
            else:
                substring = substring[substring.index(c) + 1:] + c
            #5 check max length between current max with new length of seen
            if max_length < len(substring):
                max_length = len(substring)
        return max_length
        
-----------------------------------------------------------------------------------------------------------


# Valid Parentheses (Easy):

* Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.*
Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true


    class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        
        result_list = []

        for i in range(len(s)):
            print(s[i])
            if s[i] in dict1:
                result_list.insert(0,s[i])
            elif s[i]:
                if result_list == [] :
                    return False
                if s[i] == dict1[result_list[0]]:
                    result_list.pop(0)
                else:
                    return False
        if result_list == [] :
            return True
        else:
            return False
            
-------------------------------------------------------------------------------------------------------------

# Longest Common Prefix

*Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".*

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

    class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        longest_prefix = min(strs, key = len)
        for i in range(len(strs)):
            for j in range(len(longest_prefix)):
                if strs[i][j] != longest_prefix[j]:
                    #print("i = {}, j = {}" .format(i,j))
                    longest_prefix = longest_prefix[:j]
                    #print("longest prefix = ", longest_prefix)
                    break
        return(longest_prefix)
        
-----------------------------------------------------------------------------------------------------------------

# Multiply Substrings

*Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.*

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

    class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        zero = ord('0')
        num1_integer = [(ord(num1[i]) - zero) * pow(10,len(num1) - i -1) for i in range(len(num1))]
        num2_integer = [(ord(num2[j]) - zero) * pow(10,len(num2) - j -1) for j in range(len(num2))]
        num1_integer = sum(num1_integer)
        num2_integer = sum(num2_integer)
        return str(num1_integer * num2_integer)
        
----------------------------------------------------------------------------------------------------------------------

# Reverse Words in a String (Med)
*Given an input string, reverse the string word by word.*

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

    class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        list1 = s.split(" ")
        list1 = list(filter(None, list1))
        return(" ".join(list1[::-1]))
        
----------------------------------------------------------------------------------------------------------------

# Reverse Words III
* Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.* 

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
    
    class Solution:
    def reverseWords(self, s: str) -> str:
        sent_list = s.split(" ")
        #print(sent_list)
        res_list = []
        for i in sent_list:
            res_list.append(i[::-1])
        res_string = " ".join(res_list)
        return(res_string)
-------

# Remove Sub-Folders from the Filesystem

*Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.

If a folder[i] is located within another folder[j], it is called a sub-folder of it.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.*

Example 1:
Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.

Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are subfolders of "/a".

Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]

    def removeSubfolders(folder):
        if not folder: return []
        folder.sort()
        ans, prev = [folder[0]], folder[0]+'/'
        for f in folder[1:]:
            if not f.startswith(prev):
                ans.append(f)
                prev = f+'/'
        return ans

-----
