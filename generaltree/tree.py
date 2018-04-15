import uuid
import os, sys
from multiprocessing import Queue
from . import node_info

class Tree:
    def __init__(self):
        self.height=0
        self.tree_queue=Queue()

    def add_node(self,node):
        x=1