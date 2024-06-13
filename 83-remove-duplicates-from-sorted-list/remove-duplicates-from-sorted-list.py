# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None

        slow, faster = head, head

        while faster != None:
            if slow.val == faster.val:
                faster = faster.next
            else:
                slow.next = faster
                slow = faster
                faster = faster.next
        
        slow.next = None
        
        return head
        """
        Understand: 
                    What if we have an empty list? 
                    What should return in case of an empty list?
                    What if the list only has duplicates?
                
                    Edge cases:
                                [2, 2, 3] --> [2, 3]
                                [1, 2, 3] --> [1,2, 3]

        Match:         
                    LinkedLists and two pointers: one slower and one faster
        
        Plan: 
                    1. Check if the list is empty, if it is, return None
                    2. Initialize the pointers, to start at the head
                    3. traverse through the list using the fast pointer
                    4. Compare the slow pointer with the fast pointer
                        5. If the slow pointer == fast pointer
                            we advance the fast pointer to the next position
                        6. Else slow.next == fast.pointer
                    7. We return the head

        """