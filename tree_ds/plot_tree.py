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
        plt.text(xy[0],xy[1], text, ha="center", family='sans-serif', size=9)

    def get_arrow_coordinates(self,start_loc,end_loc):
        dx=end_loc[0]-start_loc[0]
        dy=end_loc[1]-start_loc[1]   
        return (start_loc[0],start_loc[1],dx,dy)     
    
    def set_mgrid(self):
        num_of_paths=len(self.tree.paths)
        max_node_path= self.tree.height+1
        grid_size_y=complex(0,max_node_path)
        grid_size_x=complex(0,num_of_paths)
        x=0
        y=num_of_paths*0.2
        self.grid =np.mgrid[x:y:grid_size_x,x:y:grid_size_y].reshape(2, -1).T
        self.grid=self.grid[::-1] 
        self.display_grid()

    def display_grid(self):
        plt.plot(self.grid[:,0], self.grid[:,1], 'ro')

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
        tree_height=self.tree.height+1
        prev_path=-1

        path_counter=0
        path_node_counter=0

        # k is the key, path name
        # v is the list of nodes in the path
        for k,v in self.tree.paths.items():
            prev_path=-1

            # Find number of nodes to be plotted
            # Since each path would have its parent, some of the nodes would have already plotted the parent
            # We need to ignore plotting them
            nodes_to_plot_in_path=[j for j in v if j not in self.plotted ]
            print(len(nodes_to_plot_in_path))

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
                    arrow_coord=self.get_arrow_coordinates(self.grid[prev_path],self.grid[path_node_counter])
                    arrow = mpatches.Arrow(arrow_coord[0], arrow_coord[1], arrow_coord[2], arrow_coord[3],width=0.05)
                    self.patches.append(arrow)

                self.plotted[j]=path_node_counter
                prev_path=path_node_counter
                path_node_counter=path_node_counter+1                
                
            path_counter=path_counter+1
            path_node_counter=tree_height*path_counter

        self.set_plot()