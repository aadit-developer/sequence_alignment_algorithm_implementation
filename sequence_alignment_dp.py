import calcMemoryTime

s1 = 'ACACACTGACTACTGACTGGTGACTACTGACTGGACTGACTACTGACTGGTGACTACTGACTGG'
s2 = 'TATTATTATACGCTATTATACGCGACGCGGACGCGTATACGCTATTATACGCGACGCGGACGCG'

mismatch_penalty = [[0, 110, 48, 94], [110, 0, 118, 48], [48, 118, 0, 110], [94, 48, 110, 0]]
gap_penalty = 30


def seq_align(s1, s2, gap_penalty, mismatch_penalty):
    m = len(s1)
    n = len(s2)
    max_len = max(m, n)

    A = [[0 for i in range(n + 1)] for j in range(m + 1)]  # initializing the optimal value matrix

    for i in range(m):  # initializing the first row and column with gap penalties
        A[i][0] = i * gap_penalty

    for i in range(n):
        A[0][i] = i * gap_penalty

    mismatch_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}  # mapping characters to numbers in order to access their respective mismatch
                                                      # penalties

    for i in range(1, m + 1):  # parsing over both the strings in order to find minimalize the penalty
        for j in range(1, n + 1):
            if s1[i - 1] != s2[j - 1]:  # finding optimal penalty from mismatch and gap penalties
                A[i][j] = min(mismatch_penalty[mismatch_dict[s1[i - 1]]][mismatch_dict[s2[j - 1]]] + A[i - 1][j - 1],
                              gap_penalty + A[i - 1][j], gap_penalty + A[i][j - 1])
            else:
                A[i][j] = A[i - 1][j - 1]

    i = m - 1
    j = n - 1

    x_final = []
    y_final = []

    while not (i == 0 or j == 0):
        if s1[i - 1] == s2[j - 1]:
            x_final.append(s1[i - 1])
            y_final.append(s2[j - 1])
            i -= 1
            j -= 1

        elif (A[i - 1][j - 1] + mismatch_penalty[mismatch_dict[s1[i - 1]]][mismatch_dict[s2[j - 1]]]) == A[i][j]:
            x_final.append(s1[i - 1])
            y_final.append(s2[j - 1])
            i -= 1
            j -= 1

        elif (A[i - 1][j] + gap_penalty) == A[i][j]:
            x_final.append(s1[i - 1])
            y_final.append('_')
            i -= 1

        elif (A[i][j - 1] + gap_penalty) == A[i][j]:
            x_final.append('_')
            y_final.append(s2[j - 1])
            j -= 1

    x_final = ''.join(x_final[::-1])
    y_final = ''.join(y_final[::-1])

    # x_string = ''.join(x_final)
    # y_string = ''.join(y_final)

    # print(x_final[:50])
    # print(x_final[-50:])
    #
    # print(y_final[:50])
    # print(y_final[-50:])
    print(x_final)
    print(y_final)

seq_align( s1, s2, gap_penalty, mismatch_penalty)
# if __name__ == '__main__':
#     print(calcMemoryTime.run(seq_align, s1, s2, gap_penalty, mismatch_penalty))
