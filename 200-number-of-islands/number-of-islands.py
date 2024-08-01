from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Understand:
            - Check how many islands are in the list
        
        Match:
            - DFS to explore all adjacent nodes

        Plan: 
            - Check if list is empty
                Yes, we simply return 0
            - Initialize the variable to keep track of the num_islands
        """
        def dfs(r, c):
            # Check out of bounds or if the cell is water or already visited
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or
                grid[r][c] == '0' or (r, c) in visited):
                return
            visited.add((r, c))
            # Explore all adjacent nodes
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        if not grid:
            return 0

        num_islands = 0
        visited = set()

        # Row traversal
        for r in range(len(grid)):
            # Grid traversal
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    num_islands += 1
        
        return num_islands
