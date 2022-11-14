'''
695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/

Utilized classic floodfill recursive algorithm to find the maximum island in the matrix.
'''

class Solution:
    
    def __init__(self):
        ## define the directions
        self.directions = [ (-1,0), (1,0), (0,-1), (0,1) ];
    
    ## checks if location is inbound of grid dimensions
    def inbounds(self, x, y, n, m):
        return x >= 0 and y >= 0 and x < n and y < m;
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ## store dimensions
        n, m = len(grid), len(grid[0]);
        
        maximumSize = 0;
        
        ## iterate over the board
        for x in range(n):
            for y in range(m):
                
                ## if we find land
                if grid[x][y] == 1:
                    ## flood this island, count the size
                    islandSize = self.dfs(x, y, grid, n, m);
                    ## take the maximum of the max size island, and this island size
                    maximumSize = max(maximumSize, islandSize);
        
        ## return the size of the best island
        return maximumSize;
    
    ## performs the depth first search recursion (floodfill)
    def dfs(self, x, y, grid, n, m):
        
        ## unmark the current land location, this will prevent infinite recursion
        grid[x][y] = 0;

        ## the size of the further island will always include this locaiton of land itself as well.
        ## hence, start it at 1
        ans = 1;

        ## iterate over all directions
        for dx, dy in self.directions:
            ## calculate the new location after the direction change is applied
            nx, ny = x + dx, y + dy;

            ## check if the new location is inbounds of the grid dimensions and if it is land and not water (0)
            if self.inbounds(nx, ny, n, m) and grid[nx][ny] == 1:
                ## accumulate the rest of the island's size from this point further on
                ans += self.dfs(nx, ny, grid, n, m);
        
        ## return size
        return ans;


## Uncommented solution in Python3

class Solution:
    
    def __init__(self):
        self.directions = [ (-1,0), (1,0), (0,-1), (0,1) ];
    
    def inbounds(self, x, y, n, m):
        return x >= 0 and y >= 0 and x < n and y < m;
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0]);
        
        maximumSize = 0;
        
        for x in range(n):
            for y in range(m):
                
                if grid[x][y] == 1:
                    islandSize = self.dfs(x, y, grid, n, m);
                    maximumSize = max(maximumSize, islandSize);
        
        return maximumSize;
    
    def dfs(self, x, y, grid, n, m):
        
        grid[x][y] = 0;
        ans = 1;

        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy;

            if self.inbounds(nx, ny, n, m) and grid[nx][ny] == 1:
                ans += self.dfs(nx, ny, grid, n, m);
            
        return ans;