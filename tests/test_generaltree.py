import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from tree_ds import *

def test_tree_plot():
    t=Tree()

    # Add a parent node
    n=NodeInfo("Html",None,NodeType.ROOT) 
    t.add_node(n,None)

    # Add a child node
    cn=NodeInfo("head",None,None) 
    t.add_node(cn,n)

    # Add a child node
    cn1=NodeInfo("meta",None,None) 
    t.add_node(cn1,cn)    

    cn2=NodeInfo("meta",None,None) 
    t.add_node(cn2,cn)    

    cn3=NodeInfo("meta",None,None) 
    t.add_node(cn3,cn)   

    cn4=NodeInfo("meta",None,None) 
    t.add_node(cn4,cn)   
     

    cn6=NodeInfo("script",None,None) 
    t.add_node(cn6,cn)   

    cn7=NodeInfo("style",None,None) 
    t.add_node(cn7,cn) 

    cn8=NodeInfo("body",None,None) 
    t.add_node(cn8,n)   
  
    # cn9=NodeInfo("<b>",None,None) 
    # t.add_node(cn9,cn5)   
    cn5=NodeInfo("title",None,None) 
    t.add_node(cn5,cn) 

    cn10=NodeInfo("<p>",None,None) 
    t.add_node(cn10,cn5)  
    cn11=NodeInfo("<p>",None,None) 
    t.add_node(cn11,cn5)  

    #t.plot_tree()
    t.plot_tree_v2()

def test_tree_nodes():
    t=Tree()

    # Add a parent node
    n=NodeInfo("Html",None,NodeType.ROOT)
    t.add_node(n,None)

    # Add a child node
    cn=NodeInfo("head",None,None)
    t.add_node(cn,n)

    # Add a child node
    cn2=NodeInfo("js",None,None)
    t.add_node(cn2,cn)    

    # # Add a child node
    cn3=NodeInfo("body",None,None)
    t.add_node(cn3,n)    

    assert len(t.get_all_nodes())==4

def test_tree_get_node():
    t=Tree()

    # Add a parent node
    n=NodeInfo("Html",None,NodeType.ROOT)
    t.add_node(n,None)

    # Add a child node
    cn=NodeInfo("head",None,None)
    t.add_node(cn,n)

    node=t.get_node("head")

    assert node.node_key=="head","head node should be returned"

if __name__=="__main__":
    test_tree_plot()