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
        
