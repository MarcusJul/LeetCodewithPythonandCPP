# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def strtonum(ln):
            cn = ln
            lst = [cn.val]
            while(cn.next!=None):
                cn = cn.next
                lst.append(cn.val)
            s = 0
            for i in range(len(lst)-1,-1,-1):
                s *= 10
                s += lst[i]
            return s

        def numtostr(num):
            sn = ListNode(num%10)
            cn = sn
            prevn = cn
            while(num>=10):
                num = num//10
                cn = ListNode(num%10)
                prevn.next = cn
                prevn = cn
            cn.next = None
            return sn