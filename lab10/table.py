def row_sums(matrix):
    return [sum(row) for row in matrix]


def column_sums(matrix):
    if not matrix:
        return []
    return [sum(column) for column in zip(*matrix)]


def diagonal_pattern(size):
    matrix = []
    for row in range(size):
        values = []
        for column in range(size):
            if row == column:
                values.append(0)
            elif row < column:
                values.append(1)
            else:
                values.append(2)
        matrix.append(values)
    return matrix
