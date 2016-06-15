# from stack import stack
import stack


f = stack.Stack()


def test_push():
    f.push(4)
    assert f[0] == 4


def test_pop():
    assert f.pop() == 4


def test_top():
    f.push[4]
    f.push[9]
    assert f.top() == 9


def test_is_empty():
    assert f.is_empty() == True


def test_is_empty_false():
    f.push[4]
    assert f.is_empty() == False


def test_len():
    f.push[4]
    assert len(f) == 1
