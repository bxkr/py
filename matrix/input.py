def input_matrix(n: int, fill_type: type = int) -> list:
    return [list(map(fill_type, input().split())) for _ in range(n)]


if __name__ == '__main__':
    from print import print_matrix
    print_matrix(input_matrix(3))
