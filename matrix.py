class Matrix:
    def __init__(self, x_size: int, y_size: int, fill: int = None, fill_map: list = None, ranged=False):
        if ranged:
            self.matrix = (
                lambda ranged_list: [
                    ranged_list[i * x_size:(i + 1) * x_size] for i in range((len(ranged_list) + x_size - 1) // x_size)
                ])([i for i in range(1, fill + 1)])
        else:
            if fill_map is not None:
                self.matrix = fill_map
            else:
                self.matrix = [[str(fill)] * x_size] * y_size

    def __repr__(self):
        result, i = str(), int()
        for row in self.matrix:
            i += 1
            s = '\n'
            if i == len(self.matrix):
                s = ''
            result += '{}{}'.format(' '.join(map(str, row)), s)
        return result


def zeros(x_size: int, y_size: int = 0) -> Matrix:
    yr = y_size
    if yr == 0:
        yr = x_size
    return Matrix(x_size, yr, 0)


if __name__ == '__main__':
    print(zeros(3), end='\n\n')
    print(Matrix(3, 3, 9, ranged=True))
