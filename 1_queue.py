from typing import Any


class Queue:

    data: list[Any]

    def __init__(self, data: list[Any]) -> None:
        self.data = data

    def enqueue(self, item: Any) -> None:
        self.data.append(item)

    def dequeue(self) -> None:
        del self.data[0]

    def rear(self) -> Any:
        return self.data[len(self.data) - 1]

    def front(self) -> Any:
        return self.data[0]

    def __repr__(self) -> str:
        return f'Queue([{self.data}])'


# Sample Usage
q = Queue([1, 2, 3, 4, 5])
print(q)

q.enqueue(99)
q.dequeue()

q.enqueue(22)
q.dequeue()

print(q)

print('Rear:', q.rear())
print('Front:', q.front())
