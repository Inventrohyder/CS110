import numpy as np
import pandas as pd

# The DNA Strings saved as an immutable tuple
# since we wouldn't be changing its values
Set_Strings = (
    ('a', 'AGTTATGTGTCAGAGCAAAAGATTCCTCATCTAGCGGTCGCAAGTCATTGCC'),
    ('b', 'AAGTTATTTGCTCACAGGGAACGAATCCAGCTCTGCGGTCGAGGCCACATTGCC'),
    ('c', 'AGTTATTTTCAGAGAAATGATTCCTTCTCACCGGTCGAGCCAGTGCC'),
    ('d', 'AGTTTATGTGTCAGAAGCAAAAGATTACTAATCTACGCGTCGCAAGGTCTATTCC'),
    ('e', 'ACAGCTTATATAGCTCATAGGGAGCGAAATCCAGCCCCGCGGTGCGAGGCCCCTTGTCGC'),
    ('f', 'AAGTATATGGCACGAGGGAACAGTATCAGCTCTTCGGATAAAGGCCACAGTGCC'),
    ('g', 'AGTTATGTGTCACAGGCAAAAGATCCTTCTCTGCGGTCGAACCCATTGCC')
)


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
    lcs = np.zeros((m + 1, n + 1))

    # iterate through each sub problem
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs[i, j] = 0
            elif x[i - 1] == y[j - 1]:
                lcs[i, j] = lcs[i - 1, j - 1] + 1
            else:
                # use the optimal substructure property
                # of using already computed results previous subproblems
                lcs[i, j] = max(lcs[i - 1, j], lcs[i, j - 1])

    # L[m,n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return lcs[m, n]


def lcs_matrix(strings):
    """
    Generates a matrix that contains the LCS values of each string compared
    with each other string
    :param strings: An iterable containing strings to find their lcs values
    :return: The matrix of all their compared LCS values
    """
    m = np.zeros(
        # Creating an n x n matrix
        (len(strings), len(strings))
    )

    for i in range(len(strings)):
        for j in range(len(strings)):
            m[i][j] = longest_common_subsequence(
                # The DNA base sequence is the second element of each gene string
                strings[i],
                strings[j]
            )
    return m


def generate_lcs_matrix(verbose=True):
    """
    Generates the matrix that contains the LCS values of each
    DNA substring pair
    :param verbose: should we print a DataFrame representation of the matrix
    :return: an array of arrays of the lcs values
    """
    labels, strings = zip(*Set_Strings)
    m = lcs_matrix(strings)
    if verbose:
        print(pd.DataFrame(m, index=labels, columns=labels))
    return m


def relative_lcs_matrix(c, strings):
    """
    Generates a relative lcs matrix by dividing the lcs by the
    length of the given string
    :param c: The un-normalized lcs matrix
    :param strings: The set-strings used to generate the matrix c
    :return: a matrix with normalized lcs
    """
    m = np.copy(c)
    for i in range(len(strings)):
        m[i] = m[i] / len(strings[i])
    return m


def generate_relative_lcs(c, verbose=True):
    """
    Generate the relative lcs matrix of the DNA substrings
    :param c: the matrix with un-normalized lcs values
    :param verbose: should we print a DataFrame representation of the matix
    :return: an array of arrays containing the relative lcs values
    """
    labels, strings = zip(*Set_Strings)
    m = relative_lcs_matrix(c, strings)
    if verbose:
        print(pd.DataFrame(m, index=labels, columns=labels))
    return m
