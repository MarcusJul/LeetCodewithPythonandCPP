# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None:
            return head
        if head.next==None: 
            return head
        
        cur_node = head
        count=1
        node_bef, node_after = 0,0
        prev = 0
        while(cur_node!=None):
            if count==1:
                if node_bef==0: 
                    pass
                else:
                    node_bef = prev
                prev = cur_node
                cur_node = cur_node.next
                if cur_node!=None:
                    node_after = cur_node.next
                else:
                    break
                count=2
            else:
                if node_bef==0:
                    new_seq_head = cur_node
                else:
                    node_bef.next = cur_node
                cur_node.next = prev
                prev.next = node_after
                
                node_bef = prev
                cur_node = node_after
                count=1
        
        return new_seq_head