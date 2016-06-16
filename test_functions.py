import stack
from stack_functions import reverse


def test_reverse_success():
    s = stack.Stack()
    comparison_stack = stack.Stack()
    x = 0
    while x < 10:
        s.push(x)
        x = x + 1

    reversed_stack = reverse(s)

    while not reversed_stack.is_empty():
        comparison_stack.push(reversed_stack.pop())

    while not s.is_empty():
        assert s.pop() == comparison_stack.pop()


def test_reverse_unequal_pops():
    s = stack.Stack()
    comparison_stack = stack.Stack()
    x = 0
    while x < 10:
        s.push(x)
        x = x + 1

    reversed_stack = reverse(s)

    while not reversed_stack.is_empty():
        comparison_stack.push(reversed_stack.pop())

    s.push(5)

    while not s.is_empty():
        assert s.pop() != comparison_stack.pop()
