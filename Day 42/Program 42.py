class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case: If the length of the linked list is less than or equal to 1, then the list is already sorted
        if not head or not head.next:
            return head

        # Split the linked list into two halves using "slow and fast pointer" technique to find the midpoint of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # The midpoint of the linked list is slow.next
        mid = slow.next
        # Set slow.next to None to separate the left and right halves of the linked list
        slow.next = None

        # Recursively sort the left and right halves of the linked list
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the two sorted halves of the linked list
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        # Append the remaining nodes of the left or right half to the end of the sorted list
        curr.next = left or right

        return dummy.next

'''
Intuition
Approach
The approach we will use is Merge Sort:

Base Case: If the length of the linked list is less than or equal to 1, then the list is already sorted.
Split the linked list into two halves. We will use the "slow and fast pointer" technique to find the midpoint of the linked list.
Recursively sort the left and right halves of the linked list.
Merge the two sorted halves of the linked list.
Complexity
Time complexity:
O(n log n) because we are dividing the linked list in half log n times, and merging the two halves in linear time.

Space complexity:
O(log n) because the space used by the call stack during the recursive calls is log n.
'''
