from collections import deque

x = []
help(x)

# rotate array k times

l = [1, 2, 3, 4, 5, 6, 7]
l.reverse()
l.reverse(0, 3)
l.reverse(4, len(l))
print(l)
d = deque(l)
k = 3
d.rotate(k)

l[:] = list(d)

print(l)
