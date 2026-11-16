class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # base case 1
        if not grid:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
    
        # to store the number of islands, will be returning at the end
        count_islands = 0 

        # dfs method 
        def dfs(r,c):
            
            # check the boundaries first 
            if (r < 0 or c < 0 or r >=ROWS or c >= COLS):
                return 


            # base case 2, if all water in grid 
            if grid[r][c] == "0":
                return 
             
            # marking the particular r,c 0 as its land, shows we have visited it, helps to keep track
            grid[r][c] = "0"

            dfs(r - 1, c) # checks up 
            dfs(r + 1, c) # checks down 
            dfs(r, c -1 ) # checks left 
            dfs(r, c + 1) # checks right

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count_islands += 1
                    dfs(r,c)
        return count_islands



        