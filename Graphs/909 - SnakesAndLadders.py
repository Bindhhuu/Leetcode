class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = set()
        queue = deque([(1, 0)])  

        def get_coordinates(pos):
            row = (pos - 1) // n
            col = (pos - 1) % n
            if row % 2 == 1:
                col = n - 1 - col
            return n - 1 - row, col

        while queue:
            pos, moves = queue.popleft()
            for roll in range(1, 7): 
                next_pos = pos + roll
                if next_pos > n * n:
                    continue
                r, c = get_coordinates(next_pos)
                if board[r][c] != -1:
                    next_pos = board[r][c]
                if next_pos == n * n:
                    return moves + 1
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))
        return -1

