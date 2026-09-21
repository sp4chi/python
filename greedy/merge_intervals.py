class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return merged
