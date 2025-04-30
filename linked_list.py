from typing import Optional



class DoubleLinkedList:

    class Node:
        def __init__(self, value):
            self.value = value
            self.next: Optional['Node']= None
            self.prev: Optional['Node'] = None

    def __init__(self):
        self.__head: Optional['Node'] = None
        self.__tail: Optional['Node'] = None
        self.__size = 0

    def append(self, value):
        node = self.Node(value)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            node.prev = self.__tail
            self.__tail.next = node
            self.__tail = node
        self.__size += 1

    def prepend(self, value):
        node = self.Node(value)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
        self.__size += 1

    def _insert(self, value, index):
        node = self.Node(value)
        target_pointer = self.__head
        for i in range(index):
            target_pointer = target_pointer.next
        node.next = target_pointer
        node.prev = target_pointer.prev
        target_pointer.prev = node
        target_pointer.prev.next = node

    def insert(self, value, index):
        if index > self.__size or index < 0:
            raise ValueError('Index out of range')
        elif index == 0:
            self.prepend(value)
        elif index == self.__size:
            self.append(value)
        else:
            self._insert(value, index)
        self.__size += 1

    def delete(self, value):
        target_pinter = self.__head
        while target_pinter:
            if target_pinter.value == value:
                if target_pinter.prev is None:
                    self.__head = target_pinter.next
                elif target_pinter.next is None:
                    self.__tail = target_pinter.prev
                else:
                    target_pinter.prev.next = target_pinter.next
                    target_pinter.next.prev = target_pinter.prev
                self.__size -= 1
                return
            target_pinter = target_pinter.next

    def find(self, value):
        index = 0
        target_pinter = self.__head
        while target_pinter:
            if target_pinter.value == value:
                return index
            target_pinter = target_pinter.next
            index += 1
        return -1

    def __len__(self):
        return self.__size

    def __iter__(self):
        target_pinter = self.__head
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






