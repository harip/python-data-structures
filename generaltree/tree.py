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

    def get_uniq_path(self):
        return str(uuid.uuid4())

    def add_node(self,node,parent_node):
        if not parent_node is None:
            node.parent_id=parent_node.id

        if (node.type==node_type.NodeType.ROOT):
            # This is a root node
            # Create first path and add the root node
            first_path=self.get_uniq_path()
            self.paths[first_path]=[node.id]

            path_node=PathNode()
            path_node.Path=first_path
            path_node.Node=node
            path_node.NodePos=0
            self.node_belongs_to_path[node.id]=path_node

            self.root_node=node
        else:
            # Get parent path
            path=self.node_belongs_to_path[node.parent_id]

            # Location of parent in the path
            idx=path.NodePos #len(self.paths[path.Path])-1

            path_pos=idx+1
            path_name=path.Path
            if self.paths[path.Path][len(self.paths[path.Path])-1]==node.parent_id:
                # If parent is the last item in the path
                # Then the child can be attached to it                
                self.paths[path.Path].append(node.id)
            else:
                # Parent is not last item in the path
                # Create a new path (this will be a branch to a path) or new path
                new_path=self.get_uniq_path()
                path_name=new_path

                # Get the items in the existing path
                path_items=self.paths[path.Path][0:path.NodePos+1]

                self.paths[new_path]=path_items
                self.paths[new_path].append(node.id)

            # Maintain a dictionary of nodes for fast search
            path_new_node=PathNode()
            path_new_node.Path=path_name
            path_new_node.Node=node
            path_new_node.NodePos=path_pos
            self.node_belongs_to_path[node.id]=path_new_node

            if path_pos>self._height:
                self._height=path_pos

    def get_height(self):
        return self._height

    def label(self,xy, text,plt):
        y = xy[1] - 0.15  # shift y-value for label so that it's below the artist
        plt.text(xy[0], y, text, ha="center", family='sans-serif', size=14)        

    def plot_tree(self):
        pt.PlotTree().plot(self)        

class PathNode:
    def __init__(self):
        self.Path=""
        self.Node=""
        self.NodePos=0