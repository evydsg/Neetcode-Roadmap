# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1, current2 = list1, list2#Assign to the head of list1 and list2
        mergedList = ListNode(0)#Create a new listNode
        current = mergedList#To track the current nodes

        while current1 and current2:
            if current1.val <= current2.val:
                current.next = current1 #0-->current1
                current = current.next#current is now at current1
                current1 = current1.next#current1 is now the next node in the list
            else:
                current.next = current2#0-->current2
                current = current.next#current is now at current2
                current2 = current2.next#current2 is now at the next node in the list2
        
        if current2:#if current2 is not null
            current.next = current2 #current.next --> rest of the list2
        else:
            current.next = current1 #current.next --> rest of list1
        
        return mergedList.next #To return the node after the first one
