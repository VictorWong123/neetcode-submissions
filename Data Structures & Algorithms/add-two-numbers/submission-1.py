# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        curr2 = l2
        st = ""
        st2 = ""

        while curr:
            st = str(curr.val) + st
            curr = curr.next
        while curr2:
            st2 = str(curr2.val) + st2
            curr2 = curr2.next

        num = str(int(st) + int(st2))[::-1]


        dummy = ListNode()
        curr = dummy 
        for i in num:
            curr.next = ListNode(int(i))
            curr = curr.next



        return dummy.next
