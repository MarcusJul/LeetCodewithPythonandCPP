# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def strtonum(ln):
            cn = ln
            s = ln.val
            while(cn.next!=None):
                s *= 10
                cn = cn.next
                s += cn.val
            print(s)
            return s
        
        def numtolst(num):
            cn = ListNode(num%10)
            cn.next=None
            prevn = cn
            num = num//10
            while(num>0):
                cn = ListNode(num%10)
                num = num//10
                cn.next = prevn
                prevn = cn
            return cn
        return numtolst(strtonum(l1)+strtonum(l2))