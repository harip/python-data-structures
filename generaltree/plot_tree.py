import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

from . import node_info

class PlotTree:
    def __init__(self):
        plt.rcdefaults()
        self.fig, self.ax = plt.subplots()
        self.grid = np.mgrid[0.2:0.8:3j, 0.2:0.8:3j].reshape(2, -1).T
        self.patches = []

    def plot(self,nodes):
        return 0