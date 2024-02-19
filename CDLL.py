print (123)
class Node:
    def __init__(self , value):
        self.data = value
        self.next = None
        self.pre = None

class List:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    def prepend(self , value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next  = new_node
            new_node.pre = new_node
        else:
            self.head.pre = new_node
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            self.head.pre  = new_node
        self.length +=1
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node.next = new_node.pre = new_node
        else:
            new_node.pre = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.head.pre = self.tail
            self.tail.next = self.head
        self.length +=1
first = List()
first.append(10)
first.append(20)
first.append(30)

print(first)
