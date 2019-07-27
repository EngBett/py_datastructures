class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)

        if not self.empty():
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node
            self.size += 1

        else:
            self.head = new_node
            self.size += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.size += 1
        self.head = new_node

    def print(self):
        last_node = self.head
        while last_node is not None:
            print(last_node.data)
            last_node = last_node.next

    def push_to_index(self, data, index):
        if not (not (index <= self.size - 1) or not (index >= 0)):
            new_node = Node(data)
            last_node = self.head
            if index == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                i = 0
                while not index-1 == i:
                    i += 1
                    last_node = last_node.next
                new_node.next = last_node.next
                last_node.next = new_node
        else:
            print("index not found")

    def get_by_index(self, index):
        if index <= self.size - 1:
            last_node = self.head
            i = 0
            while not index == i:
                i += 1
                last_node = last_node.next
            return last_node.data
        else:
            return None

    def pop(self):
        if not self.empty():
            while self.head.next is not None:
                self.head = self.head.next
            current = self.head
            self.head = None
            return current.data
        else:
            return None

    def len(self):
        return self.size


llist = LinkedList()
llist.append(4)
llist.append(3)
llist.append(2)
llist.prepend(7)

print(llist.push_to_index(6, 1))
llist.pop()
llist.print()

