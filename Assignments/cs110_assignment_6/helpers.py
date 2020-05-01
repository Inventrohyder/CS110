def rh_get_match(x, y, k):
    """
    Finds all common length-k substrings of x and y
    using rolling hashing on both strings.
    :param x: first string
    :param y: second string
    :param k: int, length of substring
    :return: A list of tuples (i, j) where x[i:i+k] = y[j:j+k]
    """


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
