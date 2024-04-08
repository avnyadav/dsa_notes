class Heap:


    def __init__(self) -> None:
        self.data=[]

    @property
    def size(self):
        return len(self.data)
