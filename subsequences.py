# def gen_subsequences(s,i):

# 	if i == len(s):


# 	select = gen_subsequences(s,i)
# 	skip = gen_subsequences(s,i+1)


def filter(i, s):
    """Ex - 1000 -> 0100 -> 0010 -> 0001 -> 0000 stop
    suppose i = 1101 (13), s = "ABCD", mask = 1<<3 = 1000
    Now,
    1101            1101
    1000            0100
    append(s[0])    append


    """
    j = 0
    ans = []
    n = len(s)
    mask = 1 << (n - 1)  # n = 3 mask = 100
    while mask > 0:
        right_most_bit = i & mask
        if right_most_bit:
            ans.append(s[j])
        mask = mask >> 1
        j += 1
    return "".join(ans)


def generate(s):
    n = len(s)
    for i in range(1 << n):
        print("[" + filter(i, s) + "]")


generate("ABC")
