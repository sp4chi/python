def isValid(s: str) -> bool:
    n = len(s)
    if n % 2 != 0:
        return False
    stack = []

    l_brackets = {"(", "{", "["}
    r_brackets = {")", "}", "]"}

    for _ in s:
        if _ in l_brackets:
            stack.append(_)
        elif _ in r_brackets:
            stack.pop()
    return not (len(stack) > 0)


print(isValid("(())[]{}"))
