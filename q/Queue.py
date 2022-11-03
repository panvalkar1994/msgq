class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = Node(data)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError('Queue is empty')
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
