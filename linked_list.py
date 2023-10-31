from typing import Self, Any


class Node():
    index: int
    data: Any
    next: Self | Any

    def __init__(self, data: None | float = None, index: int = 0) -> None:
        self.index = index
        self.data = data
        self.next = None

    def getData(self) -> Any:
        return self.data

    def setData(self, data: Any):
        self.data = data

    def setNext(self, next: Any = None):
        self.next = next

    def getNext(self) -> Self | Any:
        return self.next

    def __repr__(self) -> str:
        if self.next:
            return f'Node(index={self.index}, data={self.data}, next=Node(data={self.next.getData()}, ...))'
        return f'Node(index={self.index}, data={self.data}, next={None})'


def getNodeLength(root: Node) -> int:
    node: Any = root
    i = 1

    if node is None:
        return i

    while node.getNext() is not None:
        node = node.getNext()
        i = i + 1
    return i


def getNodeAtIndex(index: int, root: Node) -> Node:

    node: Node | Any = root
    x = 0
    while node.getNext() is not None:
        if index == x:
            return node

        node = node.getNext()
        x = x + 1
        pass

    return node


root = Node(data=0, index=0)
node1 = Node(data=2, index=1)
node2 = Node(data=4, index=2)
node3 = Node(data=6, index=3)

root.setNext(next=node1)
node1.setNext(next=node2)
node2.setNext(next=node3)

node = getNodeAtIndex(root=root, index=3)

print(node)
