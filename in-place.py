# Source - https://stackoverflow.com/q/51804790
# Posted by Alexander, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-10, License - CC BY-SA 4.0

A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
for row in A:
    row[:] = list(map(lambda val: 1 - val, row))
print(A)
