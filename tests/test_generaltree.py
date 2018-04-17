import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from generaltree import *

def test_tree():
    t=Tree()

    # Add a parent node
    n=NodeInfo()
    n.node_key="Html"
    n.type=NodeType.ROOT    
    t.add_node(n,None)

    # Add a child node
    cn=NodeInfo()
    cn.node_key="head"
    t.add_node(cn,n)

    # Add a child node
    cn1=NodeInfo()
    cn1.node_key="body"
    t.add_node(cn1,n)    

    # Add a child node to body
    cn2=NodeInfo()
    cn2.node_key="<p>"
    t.add_node(cn2,cn1)        

    t.plot_tree()

if __name__=="__main__":
    test_tree()