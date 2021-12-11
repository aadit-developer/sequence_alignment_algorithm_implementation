import math

import sequenceAlignmentBasic

mismatch_penalty = [[0, 110, 48, 94], [110, 0, 118, 48], [48, 118, 0, 110], [94, 48, 110, 0]]
mismatch_dict = {'A': 0, 'C': 1, 'G': 2,
                 'T': 3}  # mapping characters to numbers in order to access their respective mismatch
gap_penalty = 30


def get_alignment(s1, s2):
    m = len(s1)
    n = len(s2)

    A = [[0] * (n + 1) for _ in range(2)]  # initializing the optimal value matrix

    for i in range(n + 1):
        A[1][i] = i * gap_penalty

    # penalties

    for i in range(1, m + 1):  # parsing over both the strings in order to find minimalize the penalty
        A[0] = A[1]
        A[1] = [0] * (n + 1)
        A[1][0] = A[0][0] + gap_penalty
        for j in range(1, n + 1):
            if s1[i - 1] != s2[j - 1]:  # finding optimal penalty from mismatch and gap penalties
                A[1][j] = min(mismatch_penalty[mismatch_dict[s1[i - 1]]][mismatch_dict[s2[j - 1]]] + A[0][j - 1],
                              gap_penalty + A[0][j], gap_penalty + A[1][j - 1])
            else:
                A[1][j] = A[0][j - 1]

    return A[1]


def divide_and_conquer_alignment(s1, s2):
    m = len(s1)
    n = len(s2)

    if m <= 2 or n <= 2:
        return sequenceAlignmentBasic.seq_align(s1, s2)

    mid = m // 2
    q1 = get_alignment(s1[:mid], s2)
    q2 = get_alignment(s1[mid:][::-1], s2[::-1])[::-1]
    min_num = math.inf
    q_index = -1
    for i in range(n):
        if min_num >= q1[i] + q2[i]:
            min_num = q1[i] + q2[i]
            q_index = i
    res_left, cost1 = divide_and_conquer_alignment(s1[:mid], s2[:q_index])
    res_right, cost2 = divide_and_conquer_alignment(s1[mid:], s2[q_index:])
    cost = cost1 + cost2
    return (res_left[0] + res_right[0], res_left[1] + res_right[1]), cost


def run(s1, s2):
    (res_s1, res_s2), cost = divide_and_conquer_alignment(s1, s2)
    # cost = get_alignment(s1, s2)[-1]
    return res_s1[:50], res_s1[-50:], res_s2[:50], res_s2[-50:], str(cost)

# print(run('AGT', 'ACT'))