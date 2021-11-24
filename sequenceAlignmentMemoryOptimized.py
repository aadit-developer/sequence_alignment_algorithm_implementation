import sequence_alignment_dp

s1 = 'ACACACTGACTACTGACTGGTGACTACTGACTGGACTGACTACTGACTGGTGACTACTGACTGG'
s2 = 'TATTATTATACGCTATTATACGCGACGCGGACGCGTATACGCTATTATACGCGACGCGGACGCG'

mismatch_penalty = [[0, 110, 48, 94], [110, 0, 118, 48], [48, 118, 0, 110], [94, 48, 110, 0]]
mismatch_dict = {'A': 0, 'C': 1, 'G': 2,
                 'T': 3}  # mapping characters to numbers in order to access their respective mismatch
gap_penalty = 30


def getAlignment(s1, s2):
    m = len(s1)
    n = len(s2)

    A = [[0] * (n+1) for _ in range(2)]  # initializing the optimal value matrix

    for i in range(n+1):
        A[1][i] = i * gap_penalty

    # penalties

    for i in range(1, m + 1):  # parsing over both the strings in order to find minimalize the penalty
        A[0] = A[1]
        A[1] = [0]*(n+1)
        A[1][0] = A[0][0] + gap_penalty
        for j in range(1, n + 1):
            if s1[i - 1] != s2[j - 1]:  # finding optimal penalty from mismatch and gap penalties
                A[1][j] = min(mismatch_penalty[mismatch_dict[s1[i-1]]][mismatch_dict[s2[j - 1]]] + A[0][j - 1],
                              gap_penalty + A[0][j], gap_penalty + A[1][j - 1])
            else:
                A[1][j] = A[0][j - 1]

    return A[1]

def divideAndConquerAlignment(s1, s2, res_s1 = '', res_s2 = ''):
    m = len(s1)
    n = len(s2)

    if m<=2 or n<=2:
        print(s1, s2)
        print(sequence_alignment_dp.seq_align(s1, s2, gap_penalty, mismatch_penalty))
        return sequence_alignment_dp.seq_align(s1, s2, gap_penalty, mismatch_penalty)

    mid = m//2
    q1 = [0] + getAlignment(s1[:m], s2)
    q2 = getAlignment(s1[m:][::-1], s2[::-1])[::-1] + [0]
    q = [q1[i]+q2[i] for i in range(n+1)]
    q_index = q.index(max(q)) - 1
    divideAndConquerAlignment(s1[:mid], s2[:q_index], res_s1, res_s2)
    divideAndConquerAlignment(s1[mid:], s2[q_index:], res_s1, res_s2)
    return res_s1, res_s2

divideAndConquerAlignment(s1,s2)