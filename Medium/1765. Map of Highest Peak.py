class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        heights = [[-1] * cols for _ in range(rows)]
        queue = deque()

        # Initialize the queue with water cells (height = 0)
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    heights[r][c] = 0
                    queue.append((r, c))

        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Perform BFS
        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and heights[nx][ny] == -1:
                    heights[nx][ny] = heights[x][y] + 1
                    queue.append((nx, ny))

        return heights
