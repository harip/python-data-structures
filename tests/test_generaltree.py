import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from tree_ds import *

def test_tree_plot():
    t = Tree()

    # Add a parent node
    n = NodeInfo("Html",None,NodeType.ROOT) 
    t.add_node(n,None)

    # Add a child node
    cn = NodeInfo("head",None,None) 
    t.add_node(cn,n)

    # Add a child node
    cn5 = NodeInfo("js",None,None) 
    t.add_node(cn5,cn)    

    # # Add a child node
    cn6 = NodeInfo("stylesheet",None,None) 
    t.add_node(cn6,cn)       

    # # Add a child node
    cn1 = NodeInfo("body",None,None) 
    t.add_node(cn1,n)    

    # # Add a child node to body
    cn2 = NodeInfo("<p>",None,None) 
    t.add_node(cn2,cn1)        

    # Add a child node to body
    cn3 = NodeInfo("<p>",None,None)
    t.add_node(cn3,cn1)     

    # Add a child node to body
    cn4 = NodeInfo("<p>",None,None)
    t.add_node(cn4,cn1)     
 
     # Add a child node to body
    cn7 = NodeInfo("<b>",None,None)
    t.add_node(cn7,cn4)    

    cn8 = NodeInfo("<b>",None,None)
    t.add_node(cn8,cn4)   

    assert t.height == 3,"Tree height should be 2"
    t.plot_tree()

def test_tree_nodes():
    t = Tree()

    # Add a parent node
    n = NodeInfo("Html",None,NodeType.ROOT)
    t.add_node(n,None)

    # Add a child node
    cn = NodeInfo("head",None,None)
    t.add_node(cn,n)

    # Add a child node
    cn2 = NodeInfo("js",None,None)
    t.add_node(cn2,cn)    

    # # Add a child node
    cn3 = NodeInfo("body",None,None)
    t.add_node(cn3,n)    

    assert len(t.get_all_nodes()) == 4

def test_tree_get_node():
    t = Tree()

    # Add a parent node
    n = NodeInfo("Html",None,NodeType.ROOT)
    t.add_node(n,None)

    # Add a child node
    cn = NodeInfo("head",None,None)
    t.add_node(cn,n)

    node = t.get_node("head")

    assert node.node_key == "head","head node should be returned"

if __name__ == "__main__":
    test_tree_plot()