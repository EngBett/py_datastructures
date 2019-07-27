from stack import Stack


def get_binary(num):
    stack = Stack()
    bin_string = ""
    while not num == 0:
        stack.push(str(num % 2))
        num = num // 2

    while not stack.empty():
        bin_string += stack.pop()

    return bin_string


print(get_binary(242))
print(int(get_binary(242), 2))
