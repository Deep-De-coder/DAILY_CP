class Solution:
    def search(self, nums: List[int], target: int) -> int:

        k = bisect_left(nums, True, key = lambda x: x < nums[0])  # <-- 1
 
        if target  >= nums[0]:                                    # <-- 2
            
            left = bisect_left(nums, target, hi = k-1)            # 
            return left if nums[left] == target else -1           #
                                                                  # <-- 3
        rght = bisect_left(nums, target, lo = k)                  #
        return rght if rght < len(nums) and nums[rght] == target else -1     # (this line to avoid index out of range)


'''
Here's the intuition:

If we can determinek, the so-called unknown pivot index, the solution becomes easier. The key is that nums[k] is the first element in nums that is strictly less than nums[0], so we can find it in O(logN) time with a boolean binary search.

We now have the two subrrays, nums[:k] and nums[k:], and we easily deduce in which subarray target must lie (if it indeed does lie innums) by comparing target to nums[0].

We perform a numerical binary search on the appropriate subarray, return the index if we findtarget, otherwise we return-1.

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        k = bisect_left(nums, True, key = lambda x: x < nums[0])  # <-- 1
 
        if target  >= nums[0]:                                    # <-- 2
            
            left = bisect_left(nums, target, hi = k-1)            # 
            return left if nums[left] == target else -1           #
                                                                  # <-- 3
        rght = bisect_left(nums, target, lo = k)                  #
        return rght if rght < len(nums                            # (this line to avoid index out of range)
                     ) and nums[rght] == target else -1           #
'''

