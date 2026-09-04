from collections import Counter


arr = "banana"
freq = Counter(arr)
print(freq)
print(Counter("gallahad"))
print({"map": 4, "pen": 9})
print(Counter(metal=90, pop=10))

c = Counter({"hen": 9, "duck": 10})
c["bacon"] = 7
print(c)

d = Counter("banana")
print(d.get("n"))
d["a"] = 10
print(d["a"])
print(d)
