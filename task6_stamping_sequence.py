from collections import deque


# Стирає з кінцевого рядка сумісні зі штампом ділянки в зворотному порядку.
def movesToStamp(stamp, target) -> list[int]:
    width = len(stamp)
    if not 0 < width <= len(target):
        return []

    window_count = len(target) - width + 1
    mismatches = [0] * window_count
    blocked_by = [[] for _ in target]
    ready = deque()

    for start in range(window_count):
        for offset, char in enumerate(stamp):
            position = start + offset
            if target[position] != char:
                mismatches[start] += 1
                blocked_by[position].append(start)
        if mismatches[start] == 0:
            ready.append(start)

    erased = [False] * len(target)
    remaining = len(target)
    moves = []
    while ready and remaining:
        start = ready.popleft()
        moves.append(start)
        for position in range(start, start + width):
            if erased[position]:
                continue
            erased[position] = True
            remaining -= 1
            # Стерта позиція більше не блокує жодне вікно.
            for window in blocked_by[position]:
                mismatches[window] -= 1
                if mismatches[window] == 0:
                    ready.append(window)

    return moves[::-1] if remaining == 0 else []


if __name__ == "__main__":
    for stamp, target in (
        ("abc", "ababc"),
        ("abca", "aabcaca"),
        ("a", "aaaa"),
        ("abc", "abc"),
        ("aa", "aaaaa"),
    ):
        moves = movesToStamp(stamp, target)
        assert 0 < len(moves) <= 10 * len(target)
        result = ["?"] * len(target)
        for start in moves:
            assert 0 <= start <= len(target) - len(stamp)
            result[start : start + len(stamp)] = stamp
        assert "".join(result) == target

    assert movesToStamp("abc", "ab") == []
    assert movesToStamp("ab", "aaaa") == []
    assert movesToStamp("ab", "abba") == []
    print("OK")
