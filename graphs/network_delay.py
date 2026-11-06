import heapq


def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:

    ad_list = [[] for _ in range(n + 1)]
    for u, v, d in times:
        ad_list[u].append((v, d))
    distance = [float("inf")] * (n + 1)
    distance[k] = 0

    min_heap = []
    heapq.heappush(min_heap, (0, k))

    while min_heap:
        dist, node = heapq.heappop(min_heap)

        if dist > distance[node]:
            continue

        for neighbour, weight in ad_list[node]:
            new_distance = dist + weight

            if new_distance < distance[neighbour]:
                distance[neighbour] = new_distance
                heapq.heappush(min_heap, (new_distance, neighbour))
    if float("inf") in distance[1:]:
        return -1
    return max(distance[1:])


times = [[1, 2, 1]]
n = 2
k = 2

print(networkDelayTime(times, n, k))  # expected -1

times_1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n_1 = 4
k_1 = 2
print(networkDelayTime(times_1, n_1, k_1))  # expected 2
