import uuid,sys,os 
from . import node_type

class NodeInfo:
    def __init__(self):
        self.node_id=uuid.uuid4()
        self.parent_id=self.node_id
        self.node_key=""
        self.node_val="" 
        self.type=node_type.NodeType.CHILD
        

