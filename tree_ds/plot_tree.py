# https://matplotlib.org/gallery/shapes_and_collections/artist_reference.html?highlight=matplotlib%20pyplot%20hsv

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import numpy as np

class PlotTree:
    def __init__(self):
        plt.rcdefaults()
        self.fig, self.ax = plt.subplots()
        self.grid = None
        self.patches = []
        self.tree = None
        self.plotted = dict()

    def label(self, label_xy, text):
        plt.text(label_xy[0], label_xy[1], text, ha="center", family='sans-serif', size=9)

    def get_arrow(self, start_loc, end_loc):
        return mpatches.Arrow( start_loc[0],
                                start_loc[1],
                                end_loc[0]-start_loc[0],
                                end_loc[1]-start_loc[1],
                                width=0.05)

    def set_mgrid(self):
        # Get number of paths, this will determine the width of the plot/grid
        num_of_paths = len(self.tree.paths)

        # Get the height of the tree, this will determine the height of the plot
        max_node_path = self.tree.height+1

        # Create grid
        grid_size_y = complex(0, max_node_path)
        grid_size_x = complex(0, num_of_paths)
 
        x = 0
        y = num_of_paths*0.2
        self.grid = np.mgrid[x:y:grid_size_x, x:y:grid_size_y].reshape(2, -1).T
        self.grid = self.grid[::-1]
        self.display_grid()

    def display_grid(self):
        plt.plot(self.grid[:,0], self.grid[:,1], 'ro')

    def arrange_paths(self):
        path_tuple=[(k,"-".join([self.tree.node_belongs_to_path[nv].Node.node_key for nv in v]))  for k,v in self.tree.paths.items()]
        path_tuple=sorted(path_tuple,key=lambda x:x[1])
        self.tree.paths=dict((tup[0],self.tree.paths[tup[0]]) for tup in path_tuple)

    def set_plot(self):
        colors = np.linspace(0, 1, len(self.patches))
        collection = PatchCollection(self.patches, cmap=plt.cm.hsv, alpha=0.3)
        collection.set_array(np.array(colors))
        self.ax.add_collection(collection)
        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()
        plt.show()

    def plot(self, treeds):
        """
        Main plot function to plot the nodes
            :param self:
            :param treeds: the tree data stucture
        """

        # Tree
        self.tree = treeds

        # Set the grid
        self.set_mgrid()
        tree_height=self.tree.height+1
        prev_path=-1
        node_w=0.2 

        path_counter=0
        path_node_counter=0

        # k is the key, path name
        # v is the list of nodes in the path
        for k,v in self.tree.paths.items():
            prev_path=-1
            for j in v:

                if j in self.plotted:
                    # Since path can contain the nodes that are already plotted
                    # Check if already plotted
                    prev_path = self.plotted[j]
                    path_node_counter = path_node_counter+1
                    continue

                # Draw ellipse
                ellipse = mpatches.Ellipse(self.grid[path_node_counter], node_w, 0.1)
                self.patches.append(ellipse)

                # Get text of node
                node = self.tree.node_belongs_to_path[j].Node
                self.label(self.grid[path_node_counter], node.node_key)

                # Draw arrow
                if prev_path != -1:
                    arrow_coord = self.get_arrow_coordinates(self.grid[prev_path],
                                                             self.grid[path_node_counter])
                    arrow = mpatches.Arrow(arrow_coord[0],
                                           arrow_coord[1],
                                           arrow_coord[2],
                                           arrow_coord[3],
                                           width=0.05)
                    self.patches.append(arrow)

                # Make a note of which nodes have been plotted on the chart
                self.plotted[j] = path_node_counter
                prev_path = path_node_counter
                path_node_counter = path_node_counter+1

            path_counter = path_counter+1
            path_node_counter = tree_height*path_counter

        self.set_plot()

    def plot_tree_v2(self, treeds):
        # Tree
        self.tree = treeds

        # Set the grid
        self.set_mgrid()
        node_w=0.2 

        path_counter=0
        path_node_counter=0

        self.arrange_paths()

        # k is the key, path name
        # v is the list of nodes in the path
        for k,v in self.tree.paths.items():
            node_pos_in_path=0
            for j in v:               

                # Draw ellipse
                ellipse = mpatches.Ellipse(self.grid[path_node_counter], node_w, 0.1)
                self.patches.append(ellipse)

                # Get text of node
                node = self.tree.node_belongs_to_path[j].Node
                self.label(self.grid[path_node_counter], node.node_key)

                # Draw arrow
                if node_pos_in_path != 0:
                    arrow = self.get_arrow( self.grid[path_node_counter-1],
                                            self.grid[path_node_counter])
                    self.patches.append(arrow)

                # Make a note of which nodes have been plotted on the chart
                path_node_counter = path_node_counter+1
                node_pos_in_path=node_pos_in_path+1

            # New path always starts from the top, all paths are not of same height
            path_counter = path_counter+1
            path_node_counter = (self.tree.height+1)*path_counter

        self.set_plot()
        