# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        if head.next==None :
            return head
        
        count = 2
        cnode = head.next
        midnode = head.next
        while(cnode):
            if cnode.next!=None:
                if count%2==1:
                    midnode = midnode.next
            count+=1
            cnode = cnode.next
        
        return midnode