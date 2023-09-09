class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # uq=[]
        # for x in nums:
        #     if x not in uq:
        #         uq.append(x)
        # if len(uq) == len(nums)-1:
        #     return True
        # else:
        #     return False
        # not working on [9, 9]
        n = len(nums)
        return sorted(nums) == list(range(1,n))+[n-1]   
'''
With sorted : TC / OC: O(NlogN) / O(N)

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
        n = len(nums)

        return sorted(nums) == list(range(1,n))+[n-1]
With Counter : TC / OC: O(N) / O(N)

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
        n = len(nums)

        return Counter(nums) == Counter(range(1,n)) + Counter((n-1,))
Counting : TC / OC: O(N) / O(N)
nums is a permutation of base[n] if and only if their sums, max values, and count of distinct elements are respectively equal. (It's an interesting exercise to show that sum(base[n]) = (n+3)*n//2)

class Solution:
    def isGood(self, nums: List[int]) -> bool:

        n, m, sm, mx = len(nums)-1, len(set(nums)), sum(nums), max(nums)

        return sm == (n+3)*n//2 and n == m == mx
'''
