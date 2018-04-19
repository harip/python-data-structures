import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from tree_ds import *

def test_tree_plot():
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
    cn5=NodeInfo()
    cn5.node_key="js"
    t.add_node(cn5,cn)    

    # # Add a child node
    cn6=NodeInfo()
    cn6.node_key="stylesheet"
    t.add_node(cn6,cn)       

    # # Add a child node
    cn1=NodeInfo()
    cn1.node_key="body"
    t.add_node(cn1,n)    

    # # Add a child node to body
    cn2=NodeInfo()
    cn2.node_key="<p>"
    t.add_node(cn2,cn1)        

    # Add a child node to body
    cn3=NodeInfo()
    cn3.node_key="<p>"
    t.add_node(cn3,cn1)     

    # Add a child node to body
    cn4=NodeInfo()
    cn4.node_key="<p>"
    t.add_node(cn4,cn1)     
 
     # Add a child node to body
    cn7=NodeInfo()
    cn7.node_key="<b>"
    t.add_node(cn7,cn4)    

    t.plot_tree()

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
    cn2=NodeInfo()
    cn2.node_key="js"
    t.add_node(cn2,cn)    

    # # Add a child node
    cn3=NodeInfo()
    cn3.node_key="body"
    t.add_node(cn3,n)    

    assert t.height==2,"Tree height should be 2"

def test_tree_nodes():
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
    cn2=NodeInfo()
    cn2.node_key="js"
    t.add_node(cn2,cn)    

    # # Add a child node
    cn3=NodeInfo()
    cn3.node_key="body"
    t.add_node(cn3,n)    

    assert len(t.get_all_nodes())==4

def test_tree_get_node():
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

    node=t.get_node("head")

    assert node.node_key=="head","head node should be returned"

if __name__=="__main__":
    test_tree_get_node()