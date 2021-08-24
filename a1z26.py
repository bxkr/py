def print_a1z26(*combination: int):
    alphabet = list(map(chr, range(ord('a'), ord('z')+1)))
    for number in combination:
        if number > 0:
            print(alphabet[number-1], end='')
        elif number == 0:
            print(' ', end='')
    print('\n', end='')


if __name__ == '__main__':
    print_a1z26(8, 5, 12, 12, 15, 0, 23, 15, 18, 12, 4)
