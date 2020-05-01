import mmh3
import numpy as np


def rabin_karp_matcher(target, potential, d, q):
    """
    Implements rolling hashing to find if a substring
    is present in a target string
    :param target: the target string
    :param potential: the string to detect presence of; the string potentially present
    :param d: the base number
    :param q: the number used in methods of division to generate a hash
    :return: the positions the substring is present in the target string
    """
    n = len(target)
    m = len(potential)
    h = d ** (m - 1) % q
    p = 0
    current_target_hash = 0
    occurrences = list()

    # Preprocessing
    for i in range(m):
        p = (d * p + ord(potential[i])) % q
        current_target_hash = (d * current_target_hash + ord(target[i])) % q

    # Matching
    for s in range(-1, n - m):
        if p == current_target_hash:
            if potential == target[s + 1: s + m + 1]:
                occurrences.append(s + 1)
        if s < n - m - 1:
            current_target_hash = (d * (current_target_hash - ord(target[s + 1]) * h) + ord(target[s + m + 1])) % q

    return occurrences


def rh_get_match(x, y, k, d=7, q=9):
    """
    Finds all common length-k substrings of x and y
    using rolling hashing on both strings.
    :param x: first string
    :param y: second string
    :param k: int, length of substring
    :param d: the base number to use in the rolling hash function
    :param q: the number used to divide and generate the hash value
    :return: A list of tuples (i, j) where x[i:i+k] = y[j:j+k]
    """
    n = len(x)
    m = len(y)

    output = list()

    for i in range(n - k + 1):
        matches = rabin_karp_matcher(
            target=y,
            potential=x[i:i + k],
            d=d,
            q=q
        )

        for match in matches:
            output.append((i, match))

    return output


def non_rolling_matcher(target, potential):
    """
    Finds if a substring is present in a target string without rolling
    hashes
    :param target: the target string
    :param potential: the string to detect presence of; the string potentially present
    :return: the positions the substring is present in the target string
    """
    n = len(target)
    m = len(potential)

    p = mmh3.hash(potential)

    occurrences = list()

    for s in range(n - m + 1):
        if p == mmh3.hash(target[s:s + m]):
            if potential == target[s: s + m]:
                occurrences.append(s)

    return occurrences


def regular_get_match(x, y, k):
    """
    Finds all common length-k substrings of x and y
    NOT using rolling hashing on both strings.
    :param x: first string
    :param y: second string
    :param k: int, length of substring
    :return: A list of tuples (i, j) where x[i:i+k] = y[j:j+k]
    """
    n = len(x)
    m = len(y)

    output = list()

    for i in range(n - k + 1):
        matches = non_rolling_matcher(
            target=y,
            potential=x[i:i + k]
        )

        for match in matches:
            output.append((i, match))

    return output


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
