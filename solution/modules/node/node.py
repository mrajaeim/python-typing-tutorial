from .. import Parent


class Node():
    def __init__(self) -> None:
        print("init", self.__class__.__name__)

    def some_method(self, parent: Parent):
        print("some_method", self.__class__.__name__)
        self.parent = parent
