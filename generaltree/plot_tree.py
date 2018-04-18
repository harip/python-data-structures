# https://matplotlib.org/gallery/shapes_and_collections/artist_reference.html?highlight=matplotlib%20pyplot%20hsv

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

from . import node_info
from . import tree

class PlotTree:
    def __init__(self):
        plt.rcdefaults()
        self.fig, self.ax = plt.subplots()
        self.grid = None
        self.patches = []
        self.tree=None
        self.plotted=dict()

    def label(self,xy, text):
        y = xy[1]  # shift y-value for label so that it's below the artist
        plt.text(xy[0], y, text, ha="center", family='sans-serif', size=14)
    
    def set_mgrid(self):
        num_of_paths=len(self.tree.paths)
        max_node_path= self.tree.get_height()+1

        grid_size_y=complex(0,max_node_path)
        grid_size_x=complex(0,num_of_paths)
        x=0
        y=num_of_paths*0.2
        self.grid =np.mgrid[x:y:grid_size_x,x:y:grid_size_y].reshape(2, -1).T

    def set_plot(self):
        colors = np.linspace(0, 1, len(self.patches ))
        collection = PatchCollection(self.patches , cmap=plt.cm.hsv, alpha=0.3)
        collection.set_array(np.array(colors))
        self.ax.add_collection(collection)
        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()
        plt.show()                
    
    def plot(self,tree):
        self.tree=tree
        self.set_mgrid()
        tree_height=self.tree.get_height()+1
        prev_path=-1

        path_counter=0
        path_node_counter=0
        for k,v in self.tree.paths.items():
            prev_path=-1
            for j in v:
                if j in self.plotted:
                    prev_path=self.plotted[j]
                    path_node_counter=path_node_counter+1
                    continue

                # Draw ellipse
                ellipse = mpatches.Ellipse(self.grid[path_node_counter], 0.2, 0.1)
                self.patches.append(ellipse) 

                # Get text of node
                node=self.tree.node_belongs_to_path[j].Node
                self.label(self.grid[path_node_counter], node.node_key)  

                # Draw arrow
                if prev_path!=-1:
                    start_x=self.grid[prev_path,0]
                    start_y= self.grid[prev_path,1]

                    end_x=self.grid[path_node_counter,0]
                    end_y=self.grid[path_node_counter,1]

                    dx=end_x-start_x
                    dy=end_y-start_y

                    arrow = mpatches.Arrow(self.grid[prev_path,0], self.grid[prev_path,1], dx, dy,width=0.05)
                    self.patches.append(arrow)

                self.plotted[j]=path_node_counter
                prev_path=path_node_counter
                path_node_counter=path_node_counter+1                
                
            path_counter=path_counter+1
            path_node_counter=tree_height*path_counter

        self.set_plot()