class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        count = 0
        for num in nums:
            if num == 1:
                count = count + 1 # Increment the current count when one is encountered
                max_ones = max(max_ones,count) # Update the count of maximum consecutive ones
            # If 0 is encountered, Reset the current count to 0
            else:
                count = 0
        return max_ones

        
