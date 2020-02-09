# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        prev_node = head
        cur_node = prev_node.next
        while(cur_node!=None):
            if cur_node.val == prev_node.val:
                next_node = cur_node.next
                prev_node.next = next_node
                cur_node = next_node
            else:
                prev_node = cur_node
                cur_node = prev_node.next
            
        return head
                
    
    def secondlogic(self, head:ListNode) -> ListNode:
        if head==None:
            return head
        cur_node = head
        while(cur_node!=None):
            next_node = cur_node.next
            if next_node==None:
                break
            if next_node.val == cur_node.val:
                cur_node.next = next_node.next
            else:
                cur_node = cur_node.next
        
        return head