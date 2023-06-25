class NodeD:
    def __init__(self, value:int) -> None:
        self.value = value
        self.next_node = None
        self.prev_node = None
class DoublyLinkedList:
    head:NodeD
    tail:NodeD
    count:int
    def __init__(self) -> None:
        self.head = None
        self.count = 0
        self.tail = None
    def push_beginning(self, to_be_pushed:int) -> None:
        n = NodeD(to_be_pushed)
        if self.count == 0:
            self.head = n
            self.tail = n
        else:
            x = self.head
            self.head = n
            n.next_node = x
            x.prev_node = n
        self.count += 1
    def push_end(self, to_be_pushed:int) -> None:
        n = NodeD(to_be_pushed)
        if self.count == 0:
            self.head = n
            self.tail = n
        else:
            x = self.tail
            self.tail = n
            n.prev_node = x
            x.next_node = n
        self.count += 1
    def is_empty(self) -> bool:
        return self.count == 0
    def del_end(self) -> NodeD:
        if self.is_empty():
            return None
        elif self.count == 1:
            to_return = self.tail
            self.head = None
            self.tail = None
            self.count -= 1
            return to_return
        else:
            to_return = self.tail
            next_to_last = to_return.prev_node
            next_to_last.next_node = None
            self.tail.prev_node = None
            self.count -= 1
            self.tail = next_to_last
            return to_return
    def print_doubly_linked_list(self) -> None:
        traversal = self.head
        if traversal == None:
            print("Empty linked list")
            return
        while traversal != None:
            print(traversal.value)
            traversal = traversal.next_node