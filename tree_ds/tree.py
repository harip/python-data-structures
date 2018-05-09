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

    def get_all_nodes(self):
        return [v.Node for k,v in self.node_belongs_to_path.items()]

    def get_node(self,node_name):
        nodes =[self.node_belongs_to_path[k].Node for k,v in self.node_belongs_to_path.items() if v.Node.node_key.lower() == node_name.lower()]
        return None if len(nodes)==0 else nodes[0]

    def get_node_by_uniq(self,uniq_name):
        nodes =[self.node_belongs_to_path[k].Node for k,v in self.node_belongs_to_path.items() if v.Node.uniq_name.lower() == uniq_name.lower()]
        return None if len(nodes)==0 else nodes[0]           

    def plot_tree(self):
        pt.PlotTree().plot(self)     

    def plot_tree_v2(self):
        pt.PlotTree().plot_v2(self)