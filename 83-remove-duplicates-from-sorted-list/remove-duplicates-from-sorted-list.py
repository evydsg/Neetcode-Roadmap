# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
          
        slow, fast = head, head
          
        while fast is not None:
            if slow.val == fast.val:
                fast = fast.next
            else:
                slow.next = fast
                fast = fast.next
                slow = slow.next
          
        slow.next = None
          
        return head
