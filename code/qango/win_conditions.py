
def generate_win_conditions():
    winners = [
        ## Field-Wise wins
        # Top-Left
        [0, 1, 6],
        [2, 7, 12],
        [8, 13, 14],
        # Top-Right
        [4, 5, 11],
        [3, 10, 17],
        [9, 15, 16],
        # Bottom-Left
        [24, 30, 31],
        [18, 25, 32],
        [19, 20, 26],
        # Bottom-Right
        [29, 34, 35],
        [23, 28, 33],
        [21, 22, 27],
        # Diagonal
        [0, 7, 14, 21, 28],
        [7, 14, 21, 28, 35],
        [6, 13, 20, 27, 34],
        [1, 8, 15, 22, 29],
        [5, 10, 15, 20, 25],
        [10, 15, 20, 25, 30],
        [4, 9, 14, 19, 24],
        [11, 16, 21, 26, 31]
    ]
    # Block-Wise wins
    for x in range(0, 4):
        for y in range(0, 4):
            field = x + y * 6
            winners.append([field, field + 1, field + 6, field + 7])
    # Line-Wise horizontal wins
    for x in range(0, 5):
        for y in range(0, 1):
            field = x + y * 6
            winners.append([field, field + 6, field + 12, field + 18, field + 24])
    # Line-Wise vertical wins
    for x in range(0, 1):
        for y in range(0, 5):
            field = x + y * 6
            winners.append([field, field + 1, field + 2, field + 3, field + 4])

    return winners
