# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = 0
        c=0
        ans = cur = ListNode(0)
        while l1 != None or l2 !=None:
            if l1 != None:
                temp += l1.val
                l1 = l1.next
            if l2 != None:
                temp += l2.val
                l2 = l2.next
            temp += c
            if temp >= 10:
                c=1
            else:
                c=0
            cur.next = cur = ListNode(temp%10)
            temp=0
        if c == 1:
            cur.next = cur = ListNode(c)
        return ans.next

