class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        current = self.head
        for _ in range(index):
            current = current.next
        return current.item

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if self.length == 0:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.length == 0:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            newNode = Node(val)
            current = self.head
            for _ in range(1, index):
                current = current.next
            newNode.next = current.next
            current.next = newNode
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        if index == 0:
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
        else:
            current = self.head
            for _ in range(1, index):
                current = current.next
            current.next = current.next.next
            if index == self.length - 1:
                self.tail = current

        self.length -= 1


