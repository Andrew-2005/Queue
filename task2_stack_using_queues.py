from collections import deque


# Реалізує стек однією чергою, тримаючи вершину на її початку.
class MyStack:
    # Створює порожню чергу.
    def __init__(self):
        self._queue = deque()

    # Додає елемент і переносить усі попередні елементи за нього.
    def push(self, x) -> None:
        previous_size = len(self._queue)
        self._queue.append(x)
        for _ in range(previous_size):
            self._queue.append(self._queue.popleft())

    # Виймає вершину стека з початку черги.
    def pop(self) -> int:
        return self._queue.popleft()

    # Читає вершину стека без видалення.
    def top(self) -> int:
        return self._queue[0]

    # Перевіряє, чи стек порожній.
    def empty(self) -> bool:
        return not self._queue


if __name__ == "__main__":
    stack = MyStack()
    assert stack.empty() is True
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.pop() == 2
    assert stack.empty() is False
    assert stack.pop() == 1
    assert stack.empty() is True

    stack.push(0)
    stack.push(0)
    stack.push(-1)
    assert stack.top() == -1
    assert [stack.pop() for _ in range(3)] == [-1, 0, 0]
    assert stack.empty() is True
    print("OK")
