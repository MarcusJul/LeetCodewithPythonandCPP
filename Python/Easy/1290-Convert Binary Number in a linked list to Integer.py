# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head.next==None:
            return head.val 
        if head==None:
            return None
        
        count = 1
        node = head
        s = head.val
        while(node.next!=None):
            s *= 10
            node = node.next
            s += node.val
            count+=1
        
        isum = 0
        for i in range(count):
            isum += (s%10)*2**i
            s = s//10
        return isum