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
