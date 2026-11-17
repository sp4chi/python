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

        front = {start}
        visited_front = {start}

        back = {end}
        visited_back = {end}

        moves = 0
        while front and back:
            if len(front) > len(back):
                front, back = back, front
                visited_front, visited_back = visited_back, visited_front

            # process all states in a level
            tmp = set()
            for state in front:
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

                    if new in visited_back:
                        return moves + 1

                    if new not in visited_front:
                        visited_front.add(new)
                        tmp.add(new)
            moves += 1
            front = tmp

        return -1
