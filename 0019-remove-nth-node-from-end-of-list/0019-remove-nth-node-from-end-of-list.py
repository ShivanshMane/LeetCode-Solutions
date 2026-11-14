# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Approach -  
    create a dummy node at head, which will be returned at the end, and also helpful to remove the head if needed
    initialize two pointer, slow and fast, both to the dummy node
    move fast pointers n + 1 times, so the difference between the slow and fast will be n + 1 
    then after doing this, move both the slow and fast pointers, such that fast becomes none, and slow stops right before the node which needs to be removed 
    remove the slow.next node by pointing slow.next to slow.next.next 
    and then return the dummy.next 
    Space complexity - O(1), Time complexity - O(n)
'''
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        for i in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next 
            fast = fast.next 
        slow.next = slow.next.next 
        return dummy.next


        