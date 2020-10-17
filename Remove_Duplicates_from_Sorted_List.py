# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        if head.next != None:
            front = head.next
            back = head
        else:return head
        
        
        while (1):
            if back.val == front.val:
                back.next = front.next
                front = front.next
                if back.next == None:
                    return head
                continue
            if front.next == None:
                return head
            front = front.next
            back = back.next
