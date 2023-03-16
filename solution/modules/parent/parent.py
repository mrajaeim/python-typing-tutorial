from typing import List
from .. import Node


class Parent():
    nodes: List[Node]

    def __init__(self, nodes=List[Node]) -> None:
        print("init", self.__class__.__name__)
        self.nodes = nodes
