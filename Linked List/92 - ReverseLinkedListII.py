# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next
        reverse = None

        for _ in range(right - left + 1):
            nextt = curr.next
            curr.next = reverse
            reverse = curr
            curr = nextt

        prev.next.next = curr
        prev.next = reverse

        return dummy.next  
