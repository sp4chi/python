from collections import deque


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: list[str]
    ) -> list[list[str]]:

        # Same template as word search I
        # 1. build a DAG, but reverse, child -> parent
        # 2. backtrack on dag to build output
        bank = set(wordList)

        if endWord not in bank:
            return []

        queue = deque()
        queue.append(beginWord)

        visited = {beginWord}
        dag = dict()

        found = False
        m = len(beginWord)

        while queue and not found:
            n = len(queue)

            visited_lvl = set()
            for _ in range(n):
                w = queue.popleft()

                for i in range(m):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == w[i]:
                            continue

                        mutate = w[:i] + c + w[i + 1 :]
                        if mutate == endWord:
                            found = True

                        if mutate in bank and mutate not in visited:
                            if mutate not in visited_lvl:
                                queue.append(mutate)
                                visited_lvl.add(mutate)

                            if mutate in dag:
                                dag[mutate].append(w)
                            else:
                                dag[mutate] = [w]

            visited.update(visited_lvl)

        out = []
        path = [endWord]

        def backtrack(key):
            if key == beginWord:
                out.append(path[::-1])
                return

            for parent in dag.get(key, []):
                path.append(parent)
                backtrack(parent)
                path.pop()

        if found:
            backtrack(endWord)
        return out
