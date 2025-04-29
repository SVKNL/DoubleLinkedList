class DoubleLinkedList:

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        node = self.Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def prepend(self, value):
        node = self.Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert(self, value, index):
        if index > self.size or index < 0:
            raise ValueError('Index out of range')
        elif index == 0:
            self.prepend(value)
        elif index == self.size:
            self.append(value)
        else:
            node = self.Node(value)
            target_pointer = self.head
            for i in range(index):
                target_pointer = target_pointer.next
            node.next = target_pointer
            node.prev = target_pointer.prev
            target_pointer.prev = node
            target_pointer.prev.next = node
        self.size += 1

    def delete(self, value):
        target_pinter = self.head
        while target_pinter:
            if target_pinter.value == value:
                if target_pinter.prev is None:
                    self.head = target_pinter.next
                elif target_pinter.next is None:
                    self.tail = target_pinter.prev
                else:
                    target_pinter.prev.next = target_pinter.next
                    target_pinter.next.prev = target_pinter.prev
                self.size -= 1
                return
            target_pinter = target_pinter.next

    def find(self, value):
        index = 0
        target_pinter = self.head
        while target_pinter:
            if target_pinter.value == value:
                return index
            target_pinter = target_pinter.next
            index += 1
        return -1

    def __len__(self):
        return self.size

    def __iter__(self):
        target_pinter = self.head
        while target_pinter:
            yield target_pinter.value
            target_pinter = target_pinter.next


example = DoubleLinkedList()
for i in range(10):
    example.append(i)


example.prepend(100)

example.insert(20, 1)

example.delete(3)

print(example.find(4))
print(example.find(10))
print(len(example))

for i in example:
    print(i)






