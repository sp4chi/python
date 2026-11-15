from collections import deque


class Solution:
    # def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:

    #     bank_set = set(bank)
    #     n = len(bank_set)
    #     visited = set(startGene)

    #     if endGene not in bank_set:
    #         return -1

    #     def diffWord(wordOne, wordTwo):
    #         w1 = len(wordOne)
    #         w2 = len(wordTwo)
    #         n = min(w1, w2)
    #         diff = 0
    #         for i in range(n):
    #             if wordOne[i] != wordTwo[i]:
    #                 diff += 1
    #         return diff + abs(w1-w2)

    #     queue = deque([(startGene,0)]) # word, mutation

    #     while queue:
    #         word, mutation = queue.popleft()

    #         if word == endGene:
    #             return mutation

    #         for candidate in bank_set:
    #             if candidate not in visited and diffWord(candidate,word) == 1:
    #                 visited.add(candidate)
    #                 queue.append((candidate,mutation + 1))

    #     return -1

    # time complexity - O(bank * bank)

    # Optimized - generate all possible strings, string len - 8,
    # valid characters = 'ACGT' (4), O(8*4) = O(1)
    # worst case all genes are neighbours - O(bank)

    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:

        bank_set = set(bank)
        n = len(bank_set)
        visited = set(startGene)

        if endGene not in bank_set:
            return -1

        # def diffWord(wordOne, wordTwo):
        #     w1 = len(wordOne)
        #     w2 = len(wordTwo)
        #     n = min(w1, w2)
        #     diff = 0
        #     for i in range(n):
        #         if wordOne[i] != wordTwo[i]:
        #             diff += 1
        #     return diff + abs(w1 - w2)

        queue = deque([(startGene, 0)])  # word, mutation

        while queue:
            word, mutation = queue.popleft()

            # if word == endGene:
            #     return mutation

            for _ in bank_set:
                for i in range(8):
                    for c in "ACGT":
                        if c == word[i]:
                            continue
                        new_word = word[:i] + c + word[i + 1 :]
                        if new_word not in visited and new_word in bank_set:
                            if endGene == new_word:
                                return mutation + 1
                            visited.add(new_word)
                            queue.append((new_word, mutation + 1))

        return -1
