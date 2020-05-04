import random
import string
from typing import List, Callable


def random_word(length: int) -> str:
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def empty_hash_table(N: int) -> List:
    return [[] for n in range(N)]


def add_to_hash_table(hash_table: List, item: str, hash_function: Callable[[str], int]) -> List:
    N = len(hash_table)
    index: int = hash_function(item)
    if index > N:
        index = index % N
    hash_table[index].append(item)
    return hash_table


def contains(hash_table: List, item: str, hash_function: Callable[[str], int]) -> bool:
    N = len(hash_table)
    index: int = hash_function(item)
    if index > N:
        index = index % N
    for comparison in hash_table[index]:
        if comparison == item:
            return True
    return False


def remove(hash_table: List, item: str, hash_function: Callable[[str], int]) -> List:
    if not contains(hash_table, item, hash_function):
        raise ValueError()
    index = hash_function(item)
    hash_table[index].remove(item)
    return hash_table


def hash_str1(text: str) -> int:
    ans = 0
    for chr in text:
        ans += ord(chr)
    return ans


def hash_str2(text: str) -> int:
    ans = int(ord(text[0]))
    for ix in range(1, len(text)):
        ans = ans ^ ord(text[ix])
    return int(bin(ans).split('b')[1])


def hash_str3(text: str) -> int:
    ans = 0
    for chr in text:
        ans = ans * 128 + ord(chr)
    return ans


def hash_str4(text: str) -> int:
    random.seed(ord(text[0]))
    return random.getrandbits(32)
