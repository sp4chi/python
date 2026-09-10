def divide(dividend: int, divisor: int) -> int:
    INT_MAX = (1 << 31) - 1
    INT_MIN = -(1 << 31)
    #          | div / |           |
    # dividend | chunk | remaining | count
    # 43       | 3     | 40        | 1
    # 43.      | 6.    | 37.       | 2
    # 43.      | 12.   | 31.       | 3
    # 43       | 24.   | 19.       | 4    **
    # 19.      | 3.    | 16.       | 5
    # 19       | 6     | 13        | 6
    # 19       | 12.   | 7         | 7    **
    # 7        | 3     | 4         | 8
    # 7        | 6     | 1         | 9    **

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    is_positive = (divisor > 0) == (dividend > 0)

    remaining, chunk = abs(dividend), abs(divisor)
    count = 0
    answer = 0

    while remaining >= abs(divisor):
        chunk = abs(divisor)
        count = 1

        while remaining >= (chunk << 1):
            chunk = chunk << 1
            count = count << 1

        answer += count
        remaining = remaining - chunk

    return answer if is_positive else -answer
    # k = 0
    # x = abs(dividend)
    # while x >= abs(divisor):
    #     x = x - abs(divisor)
    #     k += 1

    # if divisor < 0 and dividend < 0:
    #     return k
    # if divisor < 0:
    #     return -k
    # if dividend < 0:
    #     return -k
    # else:
    #     return k
