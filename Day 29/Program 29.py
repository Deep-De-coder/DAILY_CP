class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        
        for i in range(n):
            for j in range(n):
                # check if this is a diagonal, because
                # topleft diagonal is pattern 0,0 -> 1,1 -> 2,2 etc
                # and topright diagonal is pattern 0,2 -> 1,1 -> 2,0 etc
                if j == i or j == n-i-1:
                    # make sure nonzero
                    if grid[i][j] == 0: return False
                else:
                    # make sure zero
                    if grid[i][j] != 0: return False
                    
        # no problems
        return True
