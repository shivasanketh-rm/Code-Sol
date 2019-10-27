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