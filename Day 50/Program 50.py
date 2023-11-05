class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        
		# sort side length in descending order
        A.sort( reverse = True )
        
		# Try and test from largest side length
        for i in range( len(A) - 2):
            
            if A[i] < A[i+1] + A[i+2]:
                # Early return when we find largest perimeter triangle
                return A[i] + A[i+1] + A[i+2]
        
        # Reject: impossible to make triangle
        return 0
'''
Logic:

Sort the List to get the top 3 lengths
Check if the largest length is less than sum of other two
3. If 2 is false, drop the max length take next 3 largest length and repeat 1-2
if 2 is true, return sum of all lengths
if loop ends, and no possible combination found, return 0
'''
