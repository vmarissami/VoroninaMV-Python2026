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


def transform(matrix):
    transformed = []
    for row in matrix:
        new_row = []
        for value in row:
            if value < 0:
                value -= 2
            new_row.append(value)
        transformed.append(new_row)
    return transformed
