#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("--")
        return

    max_width = len(str(max(max(matrix, key=lambda x: max(x)))))

    for row in matrix:
        if not row:
            print("$")
        else:
            for i, num in enumerate(row):
                if i < len(row) - 1:
                    print("{:d} ".format(num), end="")
                else:
                    print("{:d}${}".format(num), end="\n" if row == matrix[-1] else "")
    print("--")
