
class Node:

    def __init__(self , value):
        self.data = value
        self.next = None

class linkedlist:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def append(self , *value):
        for item in value:
            new_node = Node(item)
            if self.head is None:
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length +=1

    def get(self , index):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self , index , value):
        node = self.get(index)
        node.data = value
    
    def remove_value(self , value):
        if self.head.data == value:
            self.head = self.head.next
        elif self.tail.data == value:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        else:
            curr = self.head
            while curr.next.data is not value:
               curr = curr.next
            curr.next = curr.next.next
    
    def remove_node(self , value):
        temp = self.head
        while temp:
            if temp.data == value:
                self.remove_value(temp.data)
            temp = temp.next
first = linkedlist()
first.append(1,1,1,1,1)
first.remove_node(2)
first.display()
