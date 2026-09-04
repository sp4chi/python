from sys import argv as args

# print("hello")

# generators

# factor
# def factor(N):
#     for num in range(1, N + 1):
#         if N % num == 0:
#             yield num


# factor(100) generates a sequence of all factors of 100.
# for fact in factor(100):
#     print(fact)

# a = input("Enter a string: ")

# N = len(a)

# b = "-"

# dash = b.join(a)
# print(dash)


# nodash = dash.replace("-", "")

# temp = dash.split("-")
# nodash = "".join(temp)
# print(nodash)

if len(args) < 2:
    print("Please provide input as. Ex - python3 demo.py 'your input'")
else:
    print(args[1:])
    str_in = " ".join(args[1:])
    first_input, *rest = str_in
    # print(first_input[1::]) #out: -R-a-v-i- in: Ravi
    # print("".join(first_input.split("-"))) #out: -R-a-v-i- in: Ravi
    print(str_in.strip(" ,."))
    str_1 = "    ,,,,.r,a.v<i...<<<"
    print(str_1.strip(" ,.<"))
    print(set(" ,,..."))


def my_strip(s, chars=" "):
    left = 0
    right = len(s) - 1

    # Convert chars into a set for O(1) lookup
    remove = set(chars)

    # Move left pointer
    while left <= right and s[left] in remove:
        print("left " + str(left))
        left += 1

    print("left pointer stops here")
    print("*" * 124)
    # Move right pointer
    while right >= left and s[right] in remove:
        print("right " + str(right))
        right -= 1
    print("right pointer stops here")
    return s[left : right + 1]


print(my_strip("....R.a.v.i,,,,,", " ....R.a.v.i,,,,, ,.<"))


def my_endswith_1(s, suffix):
    if len(suffix) > len(s):
        return False

    start = len(s) - len(suffix)

    for i in range(len(suffix)):
        if s[start + i] != suffix[i]:
            return False

    return True


def my_endswith_2(s, suffix):
    if len(suffix) > len(s):
        return False

    start = len(s) - len(suffix)

    for i in range(0, len(suffix), -1):
        if s[i] != suffix[i]:
            return False

    return True


def my_startswith(s, prefix):
    return s[: len(prefix)] == prefix


def my_endswith(s, suffix):
    return s[-len(suffix) :] == suffix


print("\n" * 2 + "running endswith")
print("Pythonxxx".endswith("xxx"))
print(my_endswith_2("Pythonxxx", "xxx"))

print("\n" * 2 + "running upper")

lower_case = "abMcNxZvAAAb123"


# ascii of 'a' is 97 and ascii of 'A' is 65, diff of 32
def my_upper(s):
    result = []
    for ch in s:
        if "a" <= ch <= "z":
            upper_ch = chr(ord(ch) - 32)
            result.append(upper_ch)
        else:
            result.append(ch)
    return "".join(result)


print(my_upper(lower_case))

print("\n" + "toggle function running")

# toggle upper to lower and lower to upper


def toggle(s):
    result = []
    for ch in s:
        if "a" <= ch <= "z":
            upper_ch = chr(ord(ch) - 32)
            result.append(upper_ch)
        elif "A" <= ch <= "Z":
            lower_ch = chr(ord(ch) + 32)
            result.append(lower_ch)
        else:
            result.append(ch)
    return "".join(result)


print(toggle(lower_case))

# str_in = "aeroplane"
# 0,1,2,3,4,5,6,7,8
# a,e,r,o,p,l,a,n,e

# print(str_in[4:9])
# print(str_in[4:])
# print(str_in[-1])
# print(str_in[-5:])  # len(str_in) + i, len(str_in)+j for -ve i,j
