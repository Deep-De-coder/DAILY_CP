# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2
        return head.next

'''
https://youtu.be/E5XXiY6QnAs
We'll create a starting node called head and use a pointer called current to traverse the two lists. At each iteration of the loop, we compare the values of the nodes at list1 and list2, and point current.next to the smaller node. Then we advance the pointers and repeat until one of the list pointers reaches the end of the list.

At this point, there's no need to iterate through the rest of the other list because we know that it's still in sorted order. So current.next = list1 or list2 points current.next to the list that still has nodes left. The last step is just to return head.next, since head was just a placeholder node and the actual list starts at head.next.

Code
