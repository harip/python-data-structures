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
from . import plot_tree as pt

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
        return 0

    def label(self,xy, text,plt):
        y = xy[1] - 0.15  # shift y-value for label so that it's below the artist
        plt.text(xy[0], y, text, ha="center", family='sans-serif', size=14)        

    def plot_tree(self):
        pt.PlotTree().plot(self.nodes)