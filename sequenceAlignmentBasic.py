mismatch_penalty = [[0, 110, 48, 94], [110, 0, 118, 48], [48, 118, 0, 110], [94, 48, 110, 0]]
mismatch_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
gap_penalty = 30


def seq_align(s1, s2):
    length_s1 = len(s1)
    length_s2 = len(s2)

    A = [[0 for i in range(length_s2 + 1)] for j in range(length_s1 + 1)]  # initializing the optimal value matrix

    for i in range(length_s1 + 1):  # initializing the first row and column with gap penalties
        A[i][0] = i * gap_penalty
    for i in range(length_s2 + 1):
        A[0][i] = i * gap_penalty

    for j in range(1, length_s2 + 1):  # parsing over both the strings in order to find minimalize the penalty
        for i in range(1, length_s1 + 1):
            if s1[i - 1] != s2[j - 1]:  # finding optimal penalty from mismatch and gap penalties
                A[i][j] = min(mismatch_penalty[mismatch_dict[s1[i - 1]]][mismatch_dict[s2[j - 1]]] + A[i - 1][j - 1],
                              gap_penalty + A[i - 1][j], gap_penalty + A[i][j - 1])
            else:
                A[i][j] = A[i - 1][j - 1]
    return get_back_trace(A, s1, s2)


def get_back_trace(A, s1, s2):
    row = len(A) - 1
    col = len(A[0]) - 1
    res_s1 = ''
    res_s2 = ''

    while row >= 1 and col >= 1:
        pen_mismatch = A[row][col] - A[row - 1][col - 1]
        pen_gap_s1 = A[row][col] - A[row][col - 1]
        pen_gap_s2 = A[row][col] - A[row - 1][col]
        row_char = s1[row - 1]
        col_char = s2[col - 1]

        if pen_mismatch == mismatch_penalty[mismatch_dict[row_char]][mismatch_dict[col_char]]:
            res_s1 = row_char + res_s1
            res_s2 = col_char + res_s2
            row -= 1
            col -= 1

        elif pen_gap_s1 == gap_penalty:
            res_s1 = '_' + res_s1
            res_s2 = col_char + res_s2
            col -= 1

        elif pen_gap_s2 == gap_penalty:
            res_s2 = '_' + res_s2
            res_s1 = row_char + res_s1
            row -= 1

    if row > 0:
        res_s1 = s1[:row] + res_s1
        res_s2 = ('_' * row) + res_s2

    if col > 0:
        res_s2 = s2[:col] + res_s2
        res_s1 = ('_' * col) + res_s1
    return res_s1, res_s2


def run(s1, s2):
    res_s1, res_s2 = seq_align(s1, s2)
    return res_s1[:50], res_s1[-50:], res_s2[:50], res_s2[-50:]
