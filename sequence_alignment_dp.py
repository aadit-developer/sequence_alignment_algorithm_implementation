# s1 = 'ACACACTGACTACTGACTGGTGACTACTGACTGGACTGACTACTGACTGGTGACTACTGACTGG'
# s2 = 'TATTATTATACGCTATTATACGCGACGCGGACGCGTATACGCTATTATACGCGACGCGGACGCG'
s1 = 'ATGGCCTC'
s2 = 'ACGGCTC'
# s1 = 'AGGGCT'
# s2 = 'AGGCA'

mismatch_penalty = [[0, 110, 48, 94], [110, 0, 118, 48], [48, 118, 0, 110], [94, 48, 110, 0]]
gap_penalty = 30


def seq_align(s1, s2, gap_penalty, mismatch_penalty):
    length_s1 = len(s1)
    length_s2 = len(s2)
    max_len = max(length_s1, length_s2)

    A = [[0 for i in range(max_len + 1)] for j in range(max_len + 1)]  #initializing the optimal value matrix

    # for i in range(length_s1):
    #     A[i][0] = i * gap_penalty
    #
    # for i in range(length_s2):
    #     A[0][i] = i * gap_penalty

    for i in range(max_len+1):              #initializing the first row and column with gap penalties
        A[i][0] = i * gap_penalty
        A[0][i] = i * gap_penalty

    mismatch_dict = {'A':0, 'C':1, 'G':2, 'T':3}        #mapping characters to numbers in order to access their respective mismatch
                                                        #penalties

    for j in range(1,length_s2+1):          #parsing over both the strings in order to find minimalize the penalty
        for i in range(1,length_s1+1):
            if s1[i-1] != s2[j-1]:          #finding optimal penalty from mismatch and gap penalties
                A[i][j] = min(mismatch_penalty[mismatch_dict[s1[i-1]]][mismatch_dict[s2[j-1]]] + A[i-1][j-1],
                              gap_penalty + A[i-1][j], gap_penalty + A[i][j-1])
            else:
                A[i][j] = A[i-1][j-1]

    print(A)


seq_align(s1, s2, gap_penalty, mismatch_penalty)