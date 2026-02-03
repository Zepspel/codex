from collections import deque


class StackTwoQueues:
    def __init__(self) -> None:
        self._q1: deque[int] = deque()
        self._q2: deque[int] = deque()

    def is_empty(self) -> bool:
        return not self._q1

    def push(self, value: int) -> None:
        self._q2.append(value)
        while self._q1:
            self._q2.append(self._q1.popleft())
        self._q1, self._q2 = self._q2, self._q1

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._q1.popleft()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._q1[0]


if __name__ == "__main__":
    stack = StackTwoQueues()
    for item in [1, 2, 3]:
        stack.push(item)
    print("Top:", stack.peek())
    while not stack.is_empty():
        print("Pop:", stack.pop())
