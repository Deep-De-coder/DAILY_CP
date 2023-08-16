class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

'''The intuition behind this function is to perform a merge similar to that in merge sort. Starting from the end of both arrays, we compare the last elements of nums1 and nums2, and place the larger element at the end of nums1. We continue this process until we have merged all the elements of nums1 and nums2.

Approach for this Problem :
Set indices i, j, and k to m - 1, n - 1, and nums1.size() - 1, respectively.
While j is greater than or equal to 0, do the following:
a. If i is greater than or equal to 0 and the element at index i in nums1 is less than or equal to the element at index j in nums2, set the element at index k in nums1 to the element at index j in nums2 and decrement j.
b. Otherwise, set the element at index k in nums1 to the element at index i in nums1 and decrement i.
Return the modified nums1.'''
