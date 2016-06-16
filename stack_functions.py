import stack


def reverse(data):
    s = stack.Stack()
    while not data.is_empty():
        s.push(data.pop())
    return s
