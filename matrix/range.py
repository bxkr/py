def range_matrix(n: int, columns: int) -> list:
    return (
        lambda ranged_list: [
            ranged_list[i * columns:(i + 1) * columns] for i in range((len(ranged_list) + columns - 1) // columns)
        ])([i for i in range(1, n+1)])
