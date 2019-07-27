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
                self.size += 1
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

    def delete_node(self, data):
        curr_node = self.head
        if curr_node and curr_node.data == data:
            self.head = curr_node.next
            curr_node = None
            self.size -= 1
            return

        prev = None
        while curr_node and curr_node.data != data:
            prev = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return
        else:
            prev.next = curr_node.next
            curr_node = None
            self.size -= 1
            return

    def pop(self):
        curr_node = self.head
        prev = None
        while curr_node.next is not None:
            prev = curr_node
            curr_node = curr_node.next

        prev.next = None
        data = curr_node.data
        curr_node = None
        self.size -= 1

        return data

    def delete_at_index(self, index):
        if self.len() >= index + 1:
            if index == self.len() - 1:
                self.pop()
            elif index == 0:
                curr = self.head
                self.head = curr.next
                curr = None
                self.size -= 1
            else:
                curr = self.head
                prev = None
                for i in range(index+1):
                    if i != 0:
                        prev = curr
                        curr = curr.next
                prev.next = curr.next
                curr = None
                self.size -= 1

        else:
            return

    def len(self):
        return self.size


llist = LinkedList()
llist.append(4)
llist.append(3)
llist.append(2)
llist.prepend(7)

llist.push_to_index(6, 1)
llist.delete_at_index(3)
llist.print()
