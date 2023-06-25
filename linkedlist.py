class Node:
    def __init__(self, value:int) -> None:
        self.value = value
        self.next_node = None
class LinkedList:
    head:Node
    count:int
    def __init__(self) -> None:
        self.head = None
        self.count = 0
    def push_end(self, to_be_pushed:int) -> None:
        self.count += 1
        if self.head == None:
            node = Node(to_be_pushed)
            self.head = node
        else:
            node = Node(to_be_pushed)
            traversal = self.head
            while traversal.next_node != None:
                traversal = traversal.next_node
            traversal.next_node = node
    def push_beginning(self, to_be_pushed:int) -> None:
        count += 1
        if self.head == None:
            node = Node(to_be_pushed)
            self.head = node
        else:
            print("spustila se druha podminka")
            node = Node(to_be_pushed)
            print("self head pred pridanim " + str(self.head))
            prev_head = self.head
            print("prev head, mel by byt to same jako self head" + str(prev_head))
            self.head = node
            print("novy self head" + str(self.head))
            print("prev head by mel zustat nezmeneny" + str(prev_head))
            self.head.next_node = prev_head
            #v linked listu je alespon jeden element
    def is_empty(self) -> bool:
        return self.head == None
    def size(self) -> int:
        return self.count
    def del_first(self) -> Node:
        if self.is_empty():
            return None
        else:
            to_return = self.head # do proměné to_return uložím odkaz na první node
            self.head = to_return.next_node #self.head bude ukazovat na prvek na který ukazoval self.head.next_node
            to_return.next_node = None #mazu referenci, kterou měl prvni node na druhý
            self.count -= 1
            return to_return
    def del_last(self) -> Node:
        if self.is_empty():
            return None
        elif self.count == 1:
            to_return = self.head
            self.head = None
            self.count -= 1
            return to_return
        else:
            traversal = self.head
            pre_traversal = None
            while traversal.next_node != None:
                pre_traversal = traversal
                traversal = traversal.next_node
            pre_traversal.next_node = None
            self.count -=1
            return traversal
    def reverse(self) -> None:
        pre_traversal = None
        traversal = self.head
        post_traversal = None
        if self.is_empty():
            return None
        if self.size() == 1:
            return None
        while traversal != None:
            post_traversal = traversal.next_node
            traversal.next_node = pre_traversal
            pre_traversal = traversal
            traversal = post_traversal
            #algoritm
        self.head = pre_traversal
        return None
    def print_linked_list(self) -> None:
        traversal = self.head
        if traversal == None:
            print("Empty linked list")
            return
        while traversal != None:
            print(traversal.value)
            traversal = traversal.next_node

        self.prev_node = None