'''
Approach - find middle, break and then reverse the second part 
    we create two nodes, slow and fast, slow pointing at head and fast at head.next 
    while fast and fast.next. at some point fast will be none and slow will be pointing at the middle 
    so store slow.next in pinter called second and break the linked list by pointing slow.next to none 
    then reverse the remaining linked list
    by creating a pointer prev which is none
    then storing the second.next in nxt 
    then second.next = prev which means it will be pointing backward 
    then changing prev to second 
    and second to nxt to follow same
    then we have two list first which is the head and second which is the prev 
    now, create two varibale to store next of first and next of second, temp1 and temp2 
    then first.next = second and second.next to tmp1
    then update first = temp1 and second to temp
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        slow = head
        fast = head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        second = slow.next 
        slow.next = None
        prev = None 
        while second:
            nxt = second.next 
            second.next = prev
            prev = second 
            second = nxt 
        
        first = head
        second = prev
        while second:
            temp1 = first.next 
            temp2 = second.next 
            first.next = second 
            second.next = temp1
            first = temp1
            second = temp2
        