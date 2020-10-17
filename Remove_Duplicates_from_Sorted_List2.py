# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        node = pre = ListNode(0)
        node.next = cur = head
        
        
        while cur.next != None:
            nex = cur.next
            if cur.val == nex.val:
                while(nex.next and nex.val == nex.next.val):
                    nex = nex.next
                pre.next = cur = nex.next
                if not cur:
                    return node.next
            else:
                pre,cur,nex = cur,nex,nex.next
        return node.next
