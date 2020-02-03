# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        head = []
        if l1==None:
            pass
        else:
            cur_l = l1
            while(True):
                head.append(cur_l.val)
                if cur_l.next==None:
                    break
                else:
                    cur_l = cur_l.next
        
        tail = []
        if l2==None:
            pass
        else:
            cur_l = l2
            while(True):
                tail.append(cur_l.val)
                if cur_l.next==None:
                    break
                else:
                    cur_l = cur_l.next
        
        mer = sorted(head+tail)
        if mer==[]:
            return None
        
        ret_l = ListNode(mer[0])
        cur_l = ret_l
        for i in range(1,len(mer)):
            l = ListNode(mer[i])
            cur_l.next = l
            cur_l = l    
        return ret_l 