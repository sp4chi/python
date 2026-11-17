from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        bank = set(wordList)

        if endWord not in bank:
            return 0

        if beginWord == endWord:
            return 0

        front = {beginWord}
        end = {endWord}

        mutations = 1
        bank.discard(beginWord)
        bank.discard(endWord)

        m = len(beginWord)
        while front and end:
            # expand the frontier with less branches
            if len(front) > len(end):
                front, end = end, front

            temp = set()

            for w in front:
                # generate valid mutations
                for i in range(m):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c in w[i]:
                            continue

                        mutate = w[:i] + c + w[i + 1 :]

                        if mutate in end:
                            return mutations + 1

                        if mutate in bank:
                            bank.discard(mutate)
                            temp.add(mutate)
            mutations += 1
            front = temp
        return 0
