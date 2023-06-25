class Stack:
    index:int
    data:list[int]
    def __init__(self) -> None:
        self.data = [] #[42]
        self.index = -1 #0
    def push(self, to_be_pushed:int) -> None:
        self.index += 1
        self.data.append(to_be_pushed)
    def pop(self) -> int:
        to_return = self.data[self.index] #42
        del self.data[self.index] #[]
        self.index -= 1 #index = -1
        return to_return
    def peek(self) -> int:
        return self.data[self.index]
    def is_empty(self) -> bool:
        return self.index == -1
    def size(self) -> int:
        return self.index + 1
class Queue:
    index:int
    data:list[int]
    def __init__(self) -> None:
        self.index = 0
        self.data = []
    def enqueue(self, to_be_added:int) -> None:
        self.data.append(to_be_added)
        self.index +=1
fronta:Queue = Queue()
fronta.enqueue(42)
fronta.enqueue(22)
print(fronta.data)