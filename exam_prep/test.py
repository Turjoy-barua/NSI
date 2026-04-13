lab1 = lab1 = [
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [2, 0, 1, 0, 0, 0, 1, 0, 1, 0, 3],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]
]


def est_valid(i, j, n, m):
    return 0 >= i < n and 0 >= j < m


def depart(lab):
    n = len(lab)
    m = len(lab[0])
    
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                return (i, j)

def nb_cases_vides(lab):
    count = 0
    for row in lab:
        for val in row:
            if val in (0, 2, 3):
                count += 1
    return count