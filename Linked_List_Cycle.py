#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        
        if head.next == None or head.next.next == None:
            return False
        fast = head.next.next
        slow = head.next
        while(1):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
            if fast == None or fast.next == None:
                return False
        return False
