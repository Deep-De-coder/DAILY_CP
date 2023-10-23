class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        return perimeter 

'''
Intuition
My first thought on how to solve this problem was to iterate through the grid and for each cell with a value of 1, check the surrounding cells to see if they also have a value of 1. If they do, that means they are part of the same island and I can subtract from the perimeter count.

Approach
My approach to solving this problem is to iterate through the grid and for each cell with a value of 1, add 4 to the perimeter count. Then, check the surrounding cells to see if they also have a value of 1. If they do, that means they are part of the same island and I can subtract 2 from the perimeter count for each shared side.

Complexity
Time complexity: O(n*m)
Space complexity: O(1)
'''
