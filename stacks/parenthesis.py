from stack import Stack


def matches(test_str):
    stack = Stack()
    for i in test_str:
        if i in "{[(":
            stack.push(i)
        else:
            if not stack.empty():
                pair = stack.peek()
                if is_pair(i, pair):
                    stack.pop()
                else:
                    return False

    return stack.empty()


def is_pair(pair, i):
    if i == "{" and pair == "}":
        return True
    elif i == "[" and pair == "]":
        return True
    elif i == "(" and pair == ")":
        return True
    else:
        return False


print(matches("{([])}"))
