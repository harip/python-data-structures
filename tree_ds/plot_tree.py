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
        """
        Node label
            :param self:
            :param label_xy: x,y location of the label
            :param text: label text
        """
        plt.text(label_xy[0], label_xy[1], text, ha="center", family='sans-serif', size=9)

    def get_arrow_coordinates(self, start_loc, end_loc):
        """
        Arrow start and end location
            :param self:
            :param start_loc: Arrow start
            :param end_loc: Arrow end
        """
        dx = end_loc[0]-start_loc[0]
        dy = end_loc[1]-start_loc[1]
        return (start_loc[0], start_loc[1], dx, dy)

    def set_mgrid(self):
        """
        Create a grid for plot layout
            :param self:
        """

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

    def set_plot(self):
        """
        Set plot parameters
            :param self:
        """
        colors = np.linspace(0, 1, len(self.patches))
        collection = PatchCollection(self.patches, cmap=plt.cm.hsv, alpha=0.3)
        collection.set_array(np.array(colors))
        self.ax.add_collection(collection)
        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()
        plt.show()

    def plot_v2(self, treeds):
        """
        Main plot function to plot the nodes
            :param self:
            :param treeds: the tree data stucture
        """

        # Tree
        self.tree = treeds

        # Set the grid
        self.set_mgrid()

        # Get some numbers
        grid_x={
            "max":max(self.grid[:,0]),
            "min":min(self.grid[:,0])
        }
        grid_y={
            "max":max(self.grid[:,1]),
            "min":min(self.grid[:,1])
        }      
        tree_height=self.tree.height+1
        prev_path=-1
        path_counter=0
        path_node_counter=0

        # dictionary of all the ellipses that need to be plotted
        to_plot=dict()

        # k is the key, path name
        # v is the list of nodes in the path
        for k,v in self.tree.paths.items():
            prev_path=-1
            prev_ellipse=tuple()
            node_pos_within_path=0
            for j in v:

                if j in self.plotted:
                    # Since path can contain the nodes that are already plotted
                    # Check if already plotted
                    prev_path = self.plotted[j]
                    prev_ellipse=(node_pos_within_path,len(to_plot[node_pos_within_path]))
                    path_node_counter = path_node_counter+1
                    node_pos_within_path=node_pos_within_path+1
                    continue

                # Draw ellipse
                ellipse = mpatches.Ellipse(self.grid[path_node_counter], 0.2, 0.1)
                # self.patches.append(ellipse)

                # Check if key exists
                if node_pos_within_path in to_plot:
                    to_plot[node_pos_within_path].append( {
                        "ellipse":ellipse,
                        "prev_ellipse_loc":prev_ellipse,
                        "node_key":self.tree.node_belongs_to_path[j].Node.node_key
                    })
                else:
                    to_plot[node_pos_within_path]=[ {
                        "ellipse":ellipse,
                        "prev_ellipse_loc":prev_ellipse,
                        "node_key":self.tree.node_belongs_to_path[j].Node.node_key
                    }]
                
                prev_ellipse=(node_pos_within_path,len(to_plot[node_pos_within_path]))
                node_pos_within_path=node_pos_within_path+1

                # Make a note of which nodes have been plotted on the chart
                self.plotted[j] = path_node_counter
                prev_path = path_node_counter
                
                path_node_counter = path_node_counter+1

            path_counter = path_counter+1
            path_node_counter = tree_height*path_counter


        # Get grid max and min
        # Total width = tot_w
        # num of items/nodes at each level = num_of_nodes
        # node width = node_w
        # num of spaces to evenly arrange the nodes = 2*num_of_nodes+1
        # every alternate space fill with node
        tot_w=grid_x["max"]-grid_x["min"] 
        node_w=0.2
        for tree_level in to_plot:
            # Ignore last level
            if tree_level==self.tree.height :
                continue

            num_of_nodes=len(to_plot[tree_level])
            num_of_spaces=2*num_of_nodes+1

            # fill the node at every even number
            space_w=tot_w/num_of_spaces
            for loc in range(1,num_of_spaces+1):
                if loc%2==0:
                    center_x= ((loc-1)*space_w) + (space_w/2)
                    # Set this center to node
                    # Get the node index
                    node_index=int(loc/2)-1
                    elip=to_plot[tree_level][node_index]["ellipse"]

                    # Y is always constant, X varies
                    elip.center[0]=1.2-center_x            

        for k in to_plot:
            for item in to_plot[k]:
                self.patches.append(item["ellipse"] )
                self.label(item["ellipse"].center, item["node_key"])  
                if len(item["prev_ellipse_loc"]) >0:
                    # Parent ellipse
                    e_key=item["prev_ellipse_loc"][0]
                    e_val_index=item["prev_ellipse_loc"][1]-1
                    parent_ellipse=to_plot[e_key][e_val_index]["ellipse"].center
                    arrow_coord = self.get_arrow_coordinates(parent_ellipse,
                                                             item["ellipse"].center)
                    arrow = mpatches.Arrow(arrow_coord[0],
                                           arrow_coord[1],
                                           arrow_coord[2],
                                           arrow_coord[3],
                                           width=0.05)        
                    self.patches.append(arrow)     
                                                                                                             

        self.set_plot()

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
                ellipse = mpatches.Ellipse(self.grid[path_node_counter], 0.2, 0.1)
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
