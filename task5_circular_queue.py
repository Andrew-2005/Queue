# Реалізує кільцеву чергу на масиві фіксованої довжини.
class MyCircularQueue:
    # Виділяє k комірок і задає початковий індекс та розмір.
    def __init__(self, k):
        self._items = [0] * k
        self._front = 0
        self._size = 0

    # Повертає перший елемент або -1 для порожньої черги.
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self._items[self._front]

    # Повертає останній елемент або -1 для порожньої черги.
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        rear = (self._front + self._size - 1) % len(self._items)
        return self._items[rear]

    # Додає значення в кінець, якщо є вільна комірка.
    def enQueue(self, value) -> bool:
        if self.isFull():
            return False
        rear = (self._front + self._size) % len(self._items)
        self._items[rear] = value
        self._size += 1
        return True

    # Видаляє перший елемент, зсуваючи початок черги.
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._front = (self._front + 1) % len(self._items)
        self._size -= 1
        return True

    # Перевіряє, чи черга порожня.
    def isEmpty(self) -> bool:
        return self._size == 0

    # Перевіряє, чи всі комірки зайняті.
    def isFull(self) -> bool:
        return self._size == len(self._items)


if __name__ == "__main__":
    queue = MyCircularQueue(3)
    assert queue.enQueue(1) is True
    assert queue.enQueue(2) is True
    assert queue.enQueue(3) is True
    assert queue.enQueue(4) is False
    assert queue.Rear() == 3
    assert queue.isFull() is True
    assert queue.deQueue() is True
    assert queue.enQueue(4) is True
    assert queue.Rear() == 4
    for value in (2, 3, 4):
        assert queue.Front() == value
        assert queue.deQueue() is True
    assert queue.isEmpty() is True

    queue = MyCircularQueue(1)
    assert queue.Front() == queue.Rear() == -1
    assert queue.deQueue() is False
    for value in (0, 9):
        assert queue.enQueue(value) is True and queue.isFull() is True
        assert queue.Front() == queue.Rear() == value
        assert queue.deQueue() is True and queue.isEmpty() is True
    print("OK")
