import uuid,sys,os 
from . import node_type

class NodeInfo:
    def __init__(self,key,val,ntype):
        self.id=str(uuid.uuid4())
        self.parent_id=self.id
        self.node_key=key
        self.node_val=val 
        self.type= node_type.NodeType.CHILD if ntype is None else ntype