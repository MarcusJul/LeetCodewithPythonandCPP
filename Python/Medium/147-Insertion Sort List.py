# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        def insertsortLinkedList(head):
            if head==None or head.next==None:
                return head
            sl = head # take the first element as the sorted list to start with
            cnode = head.next
            head.next = None # detach the sorted list from the rest
            while(cnode!=None):
                tnsl = sl #traverse node in the sorted list
                nnode = cnode.next #next node
                pre_tnsl = None # the node before tnsl
                flag = False
                while(tnsl!=None):
                    if cnode.val<=tnsl.val:
                        if pre_tnsl==None: #cnode is the smallest in the list
                            cnode.next = sl
                            sl = cnode # use cnode as the new start
                        else:
                            pre_tnsl.next = cnode
                            cnode.next = tnsl
                        break
                    else:
                        pre_tnsl = tnsl
                        tnsl = tnsl.next
                # special case where cnode is larger than any in the list
                # it becomes the last one in the list
                if tnsl==None:
                    if pre_tnsl.val<=cnode.val:
                        pre_tnsl.next = cnode
                        cnode.next = None
                cnode = nnode
            return sl
        return insertsortLinkedList(head)
        