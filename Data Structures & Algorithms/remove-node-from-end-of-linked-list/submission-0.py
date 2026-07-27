# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        left = dummy
        right = dummy

        # Move right n steps ahead
        for _ in range(n):
            right = right.next

        # Move both until right reaches the last node
        while right.next:
            left = left.next
            right = right.next

        # Delete the node
        left.next = left.next.next

        return dummy.next







        