class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_indices = {}
        
        # iterate over the array
        for i, num in enumerate(nums):
            # if the element is already in the hash map and its index difference is <= k, return True
            if num in num_indices and i - num_indices[num] <= k:
                return True
            
            # add the element to the hash map with its index
            num_indices[num] = i
        
        # if we don't find any repeated elements with the required index difference, return False
        return False

'''
Approach
One approach to solve this problem is by using a hash map. We will keep track of the indices of each element in the hash map. If we find a repeated element, we can check if the absolute difference between its current index and the previous index is less than or equal to k.

If the difference is less than or equal to k, we return true. If we iterate over the entire array and do not find any repeated elements with the required absolute difference, we return false.

Complexity
Time complexity:
Beats
96.58% O(n) since we iterate over the array once.

Space complexity:
Beats
41.62% O(min(n,k)) since we can have at most min(n,k) elements in the hash map.
'''
