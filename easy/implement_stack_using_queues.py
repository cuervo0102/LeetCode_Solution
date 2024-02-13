class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class MyStack:
    def __init__(self):
        self.rear = None
        self.front = None
        self.count = 0

    def push(self, x: int) -> None:
        new_node = Node(x)
        new_node.next = None
        if self.empty():
            self.rear = new_node
            self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.count += 1

    def pop(self) -> int:
        if self.empty():
            return 'Empty Stack'

        temp = self.front
        if self.count == 1:
            self.front = None
            self.rear = None
        else:
            while temp.next != self.rear:
                temp = temp.next
            self.rear = temp
            temp = temp.next
            self.rear.next = None
        self.count -= 1
        return temp.item

    def top(self) -> int:
        if self.empty():
            return 'Empty Stack'
        return self.rear.item

    def empty(self) -> bool:
        return self.count == 0


stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())  
print(stack.pop())  
print(stack.empty())  
