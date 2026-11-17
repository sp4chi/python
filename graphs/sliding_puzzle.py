from collections import deque


class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:

        start = "".join(str(num) for row in board for num in row)
        end = "123450"

        if start == end:
            return 0

        ad_list = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }

        queue = deque()
        queue.append(start)
        visited = {start}

        moves = 0
        while queue:
            n = len(queue)

            for _ in range(n):
                state = queue.popleft()

                # generate valid neighbours
                idx = state.index("0")
                for pos in ad_list[idx]:
                    # convert to list since strings are immutable
                    new = list(state)

                    # swap positions
                    new[idx], new[pos] = new[pos], new[idx]

                    # convert again to strings
                    new = "".join(new)
                    print(new)
                    if new == end:
                        return moves + 1

                    if new not in visited:
                        visited.add(new)
                        queue.append(new)
            moves += 1

        return -1
