"""
Basic implementation of a stack in python

Stack:
    a collection of objects insertd and removed acc. LIFO (last-in, first-out) principle

    hint: think PEZ dispenser (can only access pez at "top" of stack)

    Stack ADT formally supports:
        s.push()
            add element to the top of stack
        s.pop()
            remove and return top element from the stack; return an error if the stack is empty

    additional useful methods:
        s.top()
            return a reference to the top of the stack w/out removing it; return an error if stack empty

        s.is_empty()
            True if stack has no elements

        len(s)
            return # of items in stack


    Analysis:

        space usage: O(n)

        operation   |   running time
        ------------------------------------
        push            O(1)        * amortized bound
        pop             O(1)        * amortized bound
        top             O(1)
        is_empty        O(1)
        len             O(1)


        * occasionally an O(n)-time worst case, when the underlying Python list has to resize its internal array


    * Q: How can the design be improved?
    * Hint 1: what are the most expensive operations? What makes them (relatively) expensive?
    * Hint 2: suppose the constructor accpeted a parameter setting the value of..
"""


class Empty(Exception):
    """Error attempting to access item from an empty container."""
    pass


class Stack:

    def __init__(self):
        """Create an empty stack"""
        self._data = []    # non-public underlying Python list as storage

    def is_empty(self):
        return len(self._data) == 0

    def push(self, item):
        """Add item to the top of the stack."""
        self._data.append(item)

    def pop(self):
        """Remove and return the top item from the stack.

        Raise exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()     # calling underlying Python list's pop method

    def top(self):
        """Return the top item from the stack (but don't remove it)."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def __len__(self):
        return len(self._data)
