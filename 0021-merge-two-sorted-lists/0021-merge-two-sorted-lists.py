# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Approach - 
    Linked List problem 
    first we create a dummy node which will be storing our final merged linked list 
    and tail which will be useful to create the new list 
    first check if both list1 and list2 exists
    if yes, check if list1.val < list 2.val 
    if yes, attach the node of list 1 to tail 
    then move the list 1 pointer to list1.next which means to next node 
    same for list2
    if list2.val < list1.val 
    attach the node from list2 to tail 
    and move pointer of list2 to next node 
    then after doing this move the tail to the next node, so that next coming node can be attached to it 
    then after doing this we need to check if any one list is remaining 
    check if list1, tail.next = list1
    check if list2, tail.next = list2
    return the dummy
    time complexity - O(n + m), space complexity - O(1)
'''
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next 
            else:
                tail.next = list2
                list2 = list2.next 
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next