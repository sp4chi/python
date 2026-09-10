# find index of first occurrence of substring


def strStr(haystack: str, needle: str) -> int:
    m = len(needle)
    n = len(haystack)

    if m > n:
        return -1

    # sliding window

    for i in range(n - m + 1):
        j = 0
        k = i
        while k < n and haystack[k] == needle[j]:
            j += 1
            k += 1
            if j == m:
                return k - m

    return -1

    # i = 0
    # j = 0

    # ans = 0

    # while j < n:
    #     if haystack[j] == needle[i]:
    #         i += 1
    #         j += 1
    #         if i == m:
    #             return j - m
    #     else:
    #         j = j - i + 1
    #         i = 0

    # return -1
