x = [x for x in zip([1, 2, 3], [1, 4, 9], [1, 16, 81])]
print(x)

unzip = [unzip for unzip in zip(*x)]
print(unzip)

a, b, c = zip(*x)
print(a, b, c)

# matrix transpositon with zip

# n x n matrix
print()
print("-" * 20 + "Transpose of n x n matrix" + "-" * 20)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

transpose = [list(col) for col in zip(*matrix)]

print(transpose)

# m x n matrix
print()
print("-" * 20 + "Transpose of m x n matrix" + "-" * 20)
matrix_ = [[1, 2, 3, 4], [1, 4, 9, 16]]
print(matrix_)

transpose_ = [list(col) for col in zip(*matrix_)]
print(transpose_)
