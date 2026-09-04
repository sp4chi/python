def isValid(s: str) -> bool:
    n = len(s)
    if n % 2 != 0:
        return False
    stack = []

    l_brackets = {"(", "{", "["}

    for _ in s:
        top = stack[-1] if stack else "#"
        if _ in l_brackets:
            stack.append(_)
        elif _ == ")" and stack and top == "(":
            stack.pop()
        elif _ == "]" and stack and top == "[":
            stack.pop()
        elif _ == "}" and stack and top == "{":
            stack.pop()
        else:
            return False
    return not stack


print(isValid("(}"))
