def print_matrix(matrix: list) -> None:
    for row in matrix:
        print(*row)


if __name__ == '__main__':
    import range
    print_matrix(range.range_matrix(9, 3))
