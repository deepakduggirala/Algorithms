'''
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3466/
'''

def uniquePaths(grid, start, rem_squares):
    m = len(grid)
    n = len(grid[0])
    i,j = start
    if grid[i][j] == 2:
        return 1 if rem_squares == 0 else 0
    possible_moves = [(0,1), (0,-1), (1,0), (-1,0)]
    next_pos = [(i+dr, j+dc) for dr,dc in possible_moves if 0 <= i+dr and i+dr < m and 0 <= j+dc and j+dc < n and grid[i+dr][j+dc] in [0,2]]
    if len(next_pos) == 0:
        return 0
    else:
        sum_paths = 0
        tmp = grid[i][j]
        grid[i][j] = 1
        if tmp == 0:
            rem_squares = rem_squares - 1
        for pos in next_pos:
            num_paths = uniquePaths(grid, pos, rem_squares)
            sum_paths = sum_paths + num_paths
        grid[i][j] = tmp
        
        return sum_paths

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rem_squares = sum([1 for r in grid for c in r if c == 0])
        for i in range(len(grid)):
          for j in range(len(grid[0])):
              if grid[i][j] == 1:
                  start = (i,j)
                  break
        return uniquePaths(grid, start, rem_squares)