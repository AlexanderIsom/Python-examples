from abc import ABC, abstractmethod

#Open-closed principle

class Operations(ABC):
    @abstractmethod
    def operation():
        pass

class Last(Operations):
    def operation(list_):
        print(f"the last item in the list is {list_[len(list_)-1]}")

class Max(Operations):
    def operation(list_):
        print(f"the largest item in the list is {max(list_)}")

class Main:
    @abstractmethod
    def get_operations(list_):
        for operation in Operations.__subclasses__():
            operation.operation(list_)

Main.get_operations([1,2,8,4,5])