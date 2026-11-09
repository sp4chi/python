import heapq


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start_node: int,
        end_node: int,
    ) -> float:
        # multiplication of 2 decimals will yield a smaller value
        # now A > B and 0 <= A,B <= 1, therefore - A * 0.1 > B * 0.1
        # greedy choice - process greater probability first

        ad_list = [[] for _ in range(n)]
        for i in range(len(edges)):
            u, v = edges[i]
            ad_list[u].append((v, succProb[i]))
            ad_list[v].append((u, succProb[i]))

        best_prob = [0] * n
        best_prob[start_node] = 1

        max_heap = []

        heapq.heappush_max(max_heap, (1, start_node))

        while max_heap:
            prob, node = heapq.heappop_max(max_heap)

            if node == end_node:
                return prob

            # stale entries in heap
            if prob < best_prob[node]:
                continue

            for neighbour, intermediate_prob in ad_list[node]:
                new_prob = best_prob[node] * intermediate_prob

                if new_prob > best_prob[neighbour]:
                    best_prob[neighbour] = new_prob
                    heapq.heappush_max(max_heap, (new_prob, neighbour))

        return 0
