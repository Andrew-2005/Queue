# Реалізує двобічну чергу на масиві фіксованої довжини.
class MyCircularDeque:
    # Виділяє k комірок і задає початковий індекс та розмір.
    def __init__(self, k):
        self._items = [0] * k
        self._front = 0
        self._size = 0

    # Додає значення перед поточним початком, якщо є місце.
    def insertFront(self, value) -> bool:
        if self.isFull():
            return False
        self._front = (self._front - 1) % len(self._items)
        self._items[self._front] = value
        self._size += 1
        return True

    # Записує значення в комірку після останнього елемента.
    def insertLast(self, value) -> bool:
        if self.isFull():
            return False
        rear = (self._front + self._size) % len(self._items)
        self._items[rear] = value
        self._size += 1
        return True

    # Видаляє перший елемент, зсуваючи початок на одну комірку.
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self._front = (self._front + 1) % len(self._items)
        self._size -= 1
        return True

    # Видаляє останній елемент, зменшуючи розмір.
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self._size -= 1
        return True

    # Читає перший елемент або повертає -1 для порожньої черги.
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self._items[self._front]

    # Обчислює індекс останнього елемента та читає його.
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        rear = (self._front + self._size - 1) % len(self._items)
        return self._items[rear]

    # Перевіряє, чи в черзі немає елементів.
    def isEmpty(self) -> bool:
        return self._size == 0

    # Перевіряє, чи всі комірки зайняті.
    def isFull(self) -> bool:
        return self._size == len(self._items)


if __name__ == "__main__":
    queue = MyCircularDeque(3)
    assert queue.insertLast(1) is True
    assert queue.insertLast(2) is True
    assert queue.insertFront(3) is True
    assert queue.insertFront(4) is False
    assert queue.getRear() == 2
    assert queue.isFull() is True
    assert queue.deleteLast() is True
    assert queue.insertFront(4) is True
    assert queue.getFront() == 4
    assert queue.deleteFront() is True
    assert queue.insertLast(5) is True
    assert queue.getFront() == 3 and queue.getRear() == 5

    queue = MyCircularDeque(1)
    assert queue.isEmpty() is True
    assert queue.getFront() == queue.getRear() == -1
    assert queue.deleteFront() is False and queue.deleteLast() is False
    assert queue.insertFront(0) is True
    assert queue.insertLast(1) is False
    assert queue.getFront() == queue.getRear() == 0
    assert queue.deleteLast() is True and queue.isEmpty() is True
    assert queue.insertLast(1) is True and queue.deleteFront() is True
    print("OK")
