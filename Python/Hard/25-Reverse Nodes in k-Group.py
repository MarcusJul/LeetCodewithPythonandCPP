# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur_node = head
        s, count = [cur_node],1
        node_bef, node_after = 0,0
        
        def popStack(s):
            s = list(reversed(s))
            prev_node = 0
            for node in s:
                if node==s[0]:
                    pass
                else:
                    prev_node.next = node
                prev_node = node
            return s[0],s[-1]
        
        while(cur_node!=None):
            if count==k:
                node_after = s[-1].next
                seq_head, seq_tail = popStack(s)
                if node_bef!=0:
                    node_bef.next = seq_head
                else:
                    new_seq_head = seq_head
    
                node_bef = seq_tail
                seq_tail.next = node_after
                
                cur_node = node_after
                s,count = [cur_node], 1
                
            else:
                cur_node = cur_node.next
                s.append(cur_node)
                count+=1
            
        return new_seq_head