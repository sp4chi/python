from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:

        # using bidirectional bfs
        bank = set(bank)
        if endGene not in bank:
            return -1

        if endGene == startGene:
            return 0

        front = set()
        front.add(startGene)

        end = set()
        end.add(endGene)

        # remove seen mutations from bank
        bank.discard(startGene)
        bank.discard(endGene)

        mutations = 0
        while front and end:
            # expand the smallest frontier
            if len(front) > len(end):
                front, end = end, front

            # tmp will have all the mutations in a lvl
            # 1. python does not allow mutation of set while looping
            # 2. even if python allowed mutation, we have to process mutations in a level, without using tmp we will get incorrect no. of mutation count

            tmp = set()
            for mutation in front:
                for i in range(8):
                    for c in "ACGT":
                        if c == mutation[i]:
                            continue
                        mutate = mutation[:i] + c + mutation[i + 1 :]

                        if mutate in end:
                            return mutations + 1
                        if mutate in bank:
                            bank.discard(mutate)
                            tmp.add(mutate)
            mutations += 1
            front = tmp

        return -1
