class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       # check = [[0]*xlen for _ in range(ylen)]
        def dfs(y, x):
            if (y < 0 or y >= len(grid)) or (x < 0 or x >= len(grid[0])) or (grid[y][x] != '1'):
                return
            grid[y][x] == "0"
            
            dfs(y+1, x)
            dfs(y-1, x)
            dfs(y, x+1)
            dfs(y, x-1)
            
        xlen = len(grid[0])
        ylen = len(grid)
        island_count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    dfs(y, x)
                    island_count += 1
        
        print(island_count)


        return 0
        