import uuid
import os, sys
from multiprocessing import Queue

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

from . import node_info
from . import node_type
from . import plot_tree as pt

class Tree:
    def __init__(self):
        self._height=0
        self.paths=dict()
        self.node_belongs_to_path=dict()
        self.root_node=None

    def add_node(self,node,parent_node):
        if not parent_node is None:
            node.parent_id=parent_node.id

        if (node.type==node_type.NodeType.ROOT):
            # This is a root node
            # Create first path and add the root node
            first_path=uuid.uuid4()
            self.paths[first_path]=[node.id]
            self.node_belongs_to_path[node.id]=(first_path,node)
            self.root_node=node
        else:
            # Get parent path
            path=self.node_belongs_to_path[node.parent_id][0]

            idx=len(self.paths[path])-1
            if self.paths[path][idx]==node.parent_id:
                # If parent is the last item in the path
                # Then the child can be attached to it                
                self.paths[path].append(node.id)
            else:
                # Parent is not last item in the path
                # Create a new path (this will be a branch to a path) or new path
                new_path=uuid.uuid4()
                self.paths[new_path]=[node.id]  
                path=new_path

            # Maintain a dictionary of nodes for fast search
            self.node_belongs_to_path[node.id]=(path,node)


    def get_height(self):
        return 0

    def label(self,xy, text,plt):
        y = xy[1] - 0.15  # shift y-value for label so that it's below the artist
        plt.text(xy[0], y, text, ha="center", family='sans-serif', size=14)        

    def plot_tree(self):
        #pt.PlotTree().plot(self.nodes)
        return 0