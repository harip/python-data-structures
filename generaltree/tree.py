import uuid
from multiprocessing import Queue

from . import node_type
from . import plot_tree as pt
from . import path_node as pn

class Tree:
    def __init__(self):
        self.height=0
        self.paths=dict()
        self.node_belongs_to_path=dict()

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

            self.node_belongs_to_path[node.id]=pn.PathNode(first_path,node,0)            
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
            self.node_belongs_to_path[node.id]=pn.PathNode(path_name,node,path_pos)

            if path_pos>self.height:
                self.height=path_pos

    def plot_tree(self):
        pt.PlotTree().plot(self)     