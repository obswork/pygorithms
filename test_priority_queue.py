import priority_queue

# instantiate a new priority queue object
q = priority_queue.PriorityQueue()


def test_add():
    q.add(9, 'data')
    assert q.min() == (5, 'data')


def test_min():
    while not q.is_empty():
        q.remove_min()
    q.add(3, 'starbucks')
    q.add(8, 'caribou')
    q.add(1, 'sureshot')
    assert q.min() == (1, 'sureshot')


def test_remove_min():
    while not q.is_empty():
        q.remove_min()
    q.add(3, 'starbucks')
    q.add(8, 'caribou')
    q.add(7, 'sureshot')
    assert q.remove_min() == (3, 'starbucks')


def test_is_empty():
    # hmm..perhaps better way of testing this fn
    while not q.is_empty():
        q.remove_min()
    q.add(3, 'starbucks')
    q.remove_min()
    assert q.is_empty() == 1


def test_is_empty_false():
    while not q.is_empty():
        q.remove_min()
    q.add(4, 'target')
    assert q.is_empty() == 0


def test_len():
    while not q.is_empty():
        q.remove_min()
    q.add(5, 'walmart')
    q.add(9, 'walgreens')
    assert len(q) == 2
