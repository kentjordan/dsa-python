from typing import Any


class Stack:

    items: list[Any]

    def __init__(self) -> None:
        self.items = []

    def push(self, data: Any) -> None:
        self.items.append(data)

    def pop(self) -> Any:
        stack_len = len(self.items)

        tmp = self.items[stack_len - 1]
        self.items.remove(stack_len)

        return tmp

    def __repr__(self) -> str:
        return f'Stack([{self.items}])'


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.pop())
print(stack)

print(stack.pop())
print(stack)
