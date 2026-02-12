from abc import ABC, abstractmethod
class parent(ABC):
    @abstractmethod
    def display(self):
        pass
class son(parent):
    def display(self):
        print("this is child")
a=son()
a.display()