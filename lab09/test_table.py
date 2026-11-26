from recursion_example import factorial, factorial_iterative
from table import column_sums, diagonal_pattern, row_sums, transform

matrix = [[1, 2, 3], [4, 5, 6]]
assert row_sums(matrix) == [6, 15]
assert column_sums(matrix) == [5, 7, 9]

assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]

assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
assert column_sums([[1], [-1], [0]]) == [0]

assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []

assert diagonal_pattern(3) == [[0, 1, 1], [2, 0, 1], [2, 2, 0]]

matrix = [[-2, 0, 3], [4, -5, 6]]
original = [row.copy() for row in matrix]
result = transform(matrix)
assert result == [[-4, 0, 3], [4, -7, 6]]
result[0][0] = 99
assert matrix == original
assert result[1] is not matrix[1]
assert transform([[0, 1, -1]]) == [[0, 1, -3]]

assert factorial(0) == 1
assert factorial(5) == 120
for number in range(21):
    assert factorial(number) == factorial_iterative(number)

print("Все проверки пройдены")
