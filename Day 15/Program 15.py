class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0

        # Place non-zero elements at the start of the list
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1

        # Fill the remaining positions with zeroes
        while index < len(nums):
            nums[index] = 0
            index += 1

'''
Intuition
When approaching this problem, the idea is to perform an in-place modification of the given list of numbers. We can achieve this by first iterating through the list and moving all non-zero elements to the beginning of the list. Once we have moved all non-zero elements, we can fill the remaining positions with zeros. This approach ensures that the original order of non-zero elements is preserved while zeros are pushed to the end of the list.

Approach
Initialize a variable index to keep track of the position where the next non-zero element should be placed.
Iterate through each element num in the nums list.
If num is not equal to zero, assign num to the position index in the nums list and increment index.
After the iteration, all non-zero elements have been placed at the beginning of the list, and index indicates the position where the first zero should be placed.
Iterate from index to the end of the list, assigning zero to each position to fill the remaining positions with zeros.
By following this approach, we ensure that all non-zero elements are moved to the start of the list while maintaining their original order, and the remaining positions are filled with zeros.

Complexity
Time complexity:

The first pass through the list takes O(n) time to move non-zero elements to the start of the list.
The second pass through the list takes O(n) time to fill the remaining positions with zeros.
The overall time complexity is dominated by the linear passes through the list, resulting in O(n) time complexity.
Space complexity:

The algorithm only uses a constant amount of extra space, regardless of the input size. Hence Space complexity of this code is O(1)
It modifies the input list in-place without requiring additional data structures.
'''
