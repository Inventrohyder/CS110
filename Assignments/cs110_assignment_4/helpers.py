import numpy as np

def longest_common_subsequence(x, y):
    """
    Gives the length of the longest common substring between strings x and y
    
    :param x: The first string for lcs generation
    :param y: The second string for lcs generation
    """

    # find the length of the strings
    m = len(x)
    n = len(y)

    # declaring the array for storing the dp values
    L = np.matrix(
        np.zeros(
            (m+1, n+1)
        )
    )

    # iterate through each subproblem
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i,j] = 0
            elif x[i-1] == y[j-1]:
                L[i,j] = L[i-1,j-1]+1
            else:
                # use the optimal substructure property
                # of using already computed results previous subproblems
                L[i,j] = max(L[i-1,j] , L[i, j-1])

    # L[m,n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m, n]