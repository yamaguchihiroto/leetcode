# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        if head.next == None or head.next.next == None:
            return None
        else:
            slow = head.next
            fast = head.next.next
            
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while(slow != fast):
                    slow=slow.next
                    fast=fast.next
                return slow
        return None
