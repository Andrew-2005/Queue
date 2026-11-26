from collections import deque


# Зберігає в черзі час запитів у поточному вікні.
class RecentCounter:
    # Створює чергу для позначок часу.
    def __init__(self):
        self._requests = deque()

    # Додає запит і видаляє з початку всі записи, старші за t - 3000.
    def ping(self, t) -> int:
        self._requests.append(t)
        while self._requests[0] < t - 3000:
            self._requests.popleft()
        return len(self._requests)


if __name__ == "__main__":
    counter = RecentCounter()
    assert [counter.ping(t) for t in (1, 100, 3001, 3002)] == [1, 2, 3, 3]

    counter = RecentCounter()
    assert [counter.ping(t) for t in (1, 3001, 3002, 6002, 9003)] == [1, 2, 2, 2, 1]

    counter = RecentCounter()
    assert [counter.ping(t) for t in range(1, 3003)] == list(range(1, 3002)) + [3001]
    print("OK")
