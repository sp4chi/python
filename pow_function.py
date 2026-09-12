def my_pow(x: int, n: int) -> int:
    if n == 0:
        return 1
    if x == 0:
        return 0

    a = my_pow(x, n // 2)

    if n % 2 == 0:
        a = a * a
    else:
        a = x * a * a

    return a


def pow_(x: int, n: int) -> float:
    if n < 0:
        return 1 / my_pow(x, abs(n))
    else:
        return my_pow(x, n)


print(pow_(4, -2))
