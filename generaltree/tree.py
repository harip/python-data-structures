import uuid
import os, sys
from multiprocessing import Queue
from . import node_info

class Tree:
    def __init__(self):
        self._height=0
        self.nodes=[]

    def add_node(self,node,parent_node):
        if parent_node is not None:
            parent_node.nodes.append(node)
        else:
            self.nodes.append(node)

    def get_height(self):
        return count( node in self.nodes )