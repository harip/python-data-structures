import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import numpy as np

num_of_paths=6
max_node_path=4

grid_size_y = complex(0, max_node_path)
grid_size_x = complex(0, num_of_paths)

x = 0
y = num_of_paths*0.2
grid = np.mgrid[x:y:grid_size_x, x:y:grid_size_y].reshape(2, -1).T
grid = grid[::-1]

print(grid) 



plt.plot(grid[:,0], grid[:,1], 'ro')
plt.show()

 