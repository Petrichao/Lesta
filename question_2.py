from collections import deque


# Плюсы:
# 1. Эффективное использование памяти
# 2. Операции добавления и изъятия из очереди выполняются за О(1)
# Минусы:
# 1. Больше кода
# 2. Фксированый размер массива
class DeckFirst:
    def __init__(self, n: int):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_back(self, item):
        """Добавления элемента в конец очереди"""
        if self.size != self.max_n:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def push_front(self, item):
        """Добавления элемента в начало очереди"""
        if self.size != self.max_n:
            self.queue[self.head - 1] = item
            self.head = (self.head - 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def pop_back(self):
        """Удаление элемента с конца очереди"""
        if self.is_empty():
            IndexError("Buffer is empty")
        item = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return item

    def pop_front(self):
        """Удаление элемента с начала очереди"""
        if self.is_empty():
            IndexError("Buffer is empty")
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return item

    def is_empty(self):
        """Проверка пустая ли очередь"""
        return self.size == 0

    def is_full(self):
        """Проверка полная ли очередь"""
        return self.size == self.max_n


# Плюсы:
# 1. Меньше кода, за счет использования встроеной структуры
# 2. Гибкий объем массива
# Минусы:
# 1. Больше затраты памяти
class DeckSecond:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def enqueue(self, item):
        """Добавление элемента в очередь"""
        self.buffer.append(item)

    def dequeue(self):
        """Удаление элемента из очереди"""
        if not self.is_empty():
            return self.buffer.popleft()
        else:
            raise IndexError("Buffer is empty")

    def is_empty(self):
        """Проверка пустая ли очередь"""
        return not self.buffer

    def is_full(self):
        """Проверка полная ли очередь"""
        return len(self.buffer) == self.buffer.maxlen


if __name__ == '__main__':
    pass
