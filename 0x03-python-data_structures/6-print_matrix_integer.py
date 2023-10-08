#1/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return
    max_value = max(max(row) for row in matrix)if any(matrix) else 0
    max_width = len(str(max_value))
    for row in matrix:
        for num in row:
            print("{:>{width}}".format(num, width=max_width), end=" ")
        print()
