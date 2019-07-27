class Stack:
    def __init__(self):
        self.list = []

    def empty(self):
        return self.list == []

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if not self.empty():
            return self.list.pop(-1)

    def peek(self):
        return self.list[-1]

    def print(self):
        for i in self.list:
            print(i)