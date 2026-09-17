a = tuple(v for (k, v) in enumerate(range(1, 10)) if v % 3 == 0)
print(a)

print(ord("h"))
o = sum(ord(ch) for ch in "hollywood" if ch == "h")
print(o)


squares = sum(tuple((x**2 for x in range(1, 10))))
print(squares)


key_value = {k: v for k, v in enumerate(range(1, 10))}
print(8 in key_value)


print("hash ", hash(key_value[1]))
print(key_value)

vowels = {ch for ch in "aeroplane" if ch in "aeiou"}
vowels_with_duplicates = list(ch for ch in "aerolane" if ch in "aeiou")
print(vowels)
print(vowels_with_duplicates)

matrix = [[(row * 3) + col + 1 for col in range(3)] for row in range(3)]
print(matrix)


print("*" * 15 + "Silent Dictionary" + "*" * 15)

user = {}
l = [1, 2, 1, 22, 55, 22, 1, 6]
for el in l:
    user[el] = user.get(el, 0) + 1
# print(user["new_key"])
print(user)

print(
    "*" * 15 + "Target Sum" + "*" * 15,
)

nums = [1, 2, 1, 22, 25, 22, 22, 22]
temp = {}
target = 44

for k, v in enumerate(nums):
    residue = target - v
    if residue in temp:
        print([temp.get(residue), k])
        break
    else:
        temp[v] = k
print(temp)


# in-place sort
l.sort()
print(l)

# copies, sorts then returns list
sort_ = sorted(l)
print(sort_)

print()
print("*" * 15 + "Word Count" + "*" * 15)

s = "Grace Anna Coolidge (née Goodhue; January 3, 1879 – July 8, 1957) was first lady of the United States from 1923 to 1929 as the wife of the 30th president of the United States, Calvin Coolidge. She was previously the second lady of the United States from 1921 to 1923 and the first lady of Massachusetts from 1919 to 1921."

word_cnt = {}
for word in s.split():
    word_cnt[word] = word_cnt.get(word, 0) + 1

print(word_cnt)

print(word_cnt.get("kaushik", 1))

# help(word_cnt)

from collections import Counter

word_counter = Counter(
    s.split(),
)
print(word_counter)

# help(word_counter)

from collections import deque

deq = deque([1, 2, 3, 4, 5, 6, 7])

deq.rotate()
deq.rotate()
deq.rotate()

print(deq)
