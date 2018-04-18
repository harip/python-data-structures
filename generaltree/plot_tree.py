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
        self.grid = np.mgrid[0.2:0.8:3j, 0.2:0.8:3j].reshape(2, -1).T
        self.patches = []
        self.tree=None
        self.plotted=dict()

    def label(self,xy, text):
        y = xy[1] - 0.15  # shift y-value for label so that it's below the artist
        plt.text(xy[0], y, text, ha="center", family='sans-serif', size=14)
    
    def get_mgrid(self):
        num_of_paths=len(self.tree.paths)
        max_node_path= self.tree.get_height()+1

        grid_size_y=complex(0,max_node_path)
        grid_size_x=complex(0,num_of_paths)
        tree_grid=np.mgrid[0.2:0.8:grid_size_x, 0.2:0.8:grid_size_y].reshape(2, -1).T
        return tree_grid
    
    def plot(self,tree):
        self.tree=tree
        plot_grid=self.get_mgrid()
        patches = []
        tree_height=self.tree.get_height()+1

        path_counter=0
        path_node_counter=0
        for k,v in self.tree.paths.items():
            
            for j in v:
                if j in self.plotted:
                    path_node_counter=path_node_counter+1
                    continue

                ellipse = mpatches.Ellipse(plot_grid[path_node_counter], 0.2, 0.1)
                patches.append(ellipse) 
                self.label(plot_grid[path_node_counter], path_node_counter)  
                path_node_counter=path_node_counter+1
                
                self.plotted[j]=True

            path_counter=path_counter+1
            path_node_counter=tree_height*path_counter
 
        colors = np.linspace(0, 1, len(patches))
        collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3)
        collection.set_array(np.array(colors))
        self.ax.add_collection(collection)

        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()

        plt.show()                