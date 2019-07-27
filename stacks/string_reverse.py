from stack import Stack


def reverse(my_str):
    result = ""
    stack = Stack()
    for i in my_str:
        stack.push(i)
    while not stack.empty():
        result += stack.pop()

    return result


print(reverse("Hello Jimmy"))
