# from stack import stack
import stack


f = stack.Stack()


def test_push_pop():
    f.push(4)
    assert f.pop() == 4


def test_top():
    f.push(4)
    f.push(9)
    assert f.top() == 9


def test_is_empty():
    while not f.is_empty():
        f.pop()
    assert f.is_empty() == 1


def test_is_empty_false():
    f.push(4)
    assert f.is_empty() == 0


def test_len():
    while not f.is_empty():
        f.pop()
    f.push(4)
    assert len(f) == 1
