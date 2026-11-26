from collections import Counter


# Підраховує символи й повертає індекс першого, що трапляється один раз.
def firstUniqChar(s) -> int:
    counts = Counter(s)
    for index, char in enumerate(s):
        if counts[char] == 1:
            return index
    return -1


if __name__ == "__main__":
    assert firstUniqChar("leopard") == 0
    assert firstUniqChar("loveleopard") == 2
    assert firstUniqChar("aabb") == -1
    assert firstUniqChar("") == -1
    assert firstUniqChar("x") == 0
    assert firstUniqChar("aaaab") == 4
    print("OK")
