def longest_substring_with_atmost_k_distinct_characters(s: str, k: int) -> int:
    """Track the no. of dictinct elements"""
    unique, left, right, ans, distinct = {}, 0, 0, 0, 0

    while right < len(s):
        unique[s[right]] = unique.get(s[right], 0) + 1

        while len(unique) > k:
            unique[s[left]] = unique.get(s[left]) - 1

            if unique[s[left]] == 0:
                del unique[s[left]]
            left += 1

        ans = max(ans, right - left + 1)
        right += 1

    return ans


print(longest_substring_with_atmost_k_distinct_characters(s="eceba", k=2))
