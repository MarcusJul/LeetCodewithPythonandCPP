class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        width, length = len(grid[0]), len(grid)
        i,j = 0,0
        pool = [[0]*width for i in range(length)]
        
        for i in range(length):
            for j in range(width):
                if i==0:
                    if j!=0:
                        pool[i][j] = pool[i][j-1]+grid[i][j]
                    else:
                        pool[i][j] = grid[i][j]
                else:#
                    if j!=0:
                        pool[i][j] = min(pool[i][j-1],pool[i-1][j])+grid[i][j]
                    else:
                        pool[i][j] = pool[i-1][j]+grid[i][j]
            
        return pool[i][j]
        
        
