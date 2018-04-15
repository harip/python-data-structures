import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from generaltree import *

def test_tree():
    t=Tree()
    n=NodeInfo()
    
    print(t.height)

if __name__=="__main__":
    test_tree()