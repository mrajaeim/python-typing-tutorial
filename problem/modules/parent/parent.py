from typing import List
from .. import Node


class Parent():
    nodes: List[Node]

    def __init__(self, nodes=List[Node]) -> None:
        self.nodes = nodes
