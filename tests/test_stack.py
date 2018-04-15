import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from stack import Stack

def test_stack_peek():
    s=Stack()
    s.push(1)
    s.push(2)

    assert s.peek()==2,"Peek value should be 2"

def test_stack_size():
    s=Stack()
    s.push(1)
    s.push(2)

    assert s.size()==2,"Size of stack should be 2"

def test_stack_pop():
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    assert s.pop()==4,"Pop should remove the latest item pushed which is 4"    