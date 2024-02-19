class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        self.pre = None

class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
        result = ""
        temp = self.head
        while temp is not None:
            result += str(temp.data)
            if temp.next is not None:
                result += ' <-> '
            temp = temp.next
        return result

    def append(self ,value):
        new_node = Node(value)
        if self.head is None:
           self.head = new_node
           self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.pre = self.tail
            self.tail = new_node
        self.length +=1
    def prepend(self , value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.pre = new_node
            self.head = new_node
        self.length +=1
    def delete_by_key(self , value):
        if self.head is None:
            return None
        elif self.length ==1:
            self.head = self.tail = None
        elif self.head.data == value:
            self.head = self.head.next
            self.head.pre = None
        elif self.tail.data == value:
            self.tail = self.tail.pre
            self.tail.next = None
        else:
            curr = self.head
            while curr.data is not value:
                curr = curr.next
            curr.pre.next = curr.next
            curr.next.pre = curr.pre
        self.length -=1
    def remove_all_nodes(self,value):
        ...
    def remove_even(self):
        temp = self.head
        for x in range(1,self.length +1):
            if x % 2 == 0:
                self.delete_by_key(temp.data)
            temp = temp.next

first = linked_list()
first.append(1)
first.append(2)
first.append(3)
first.append(4)
first.append(5)
first.append(6)
first.remove_even()
print(first)
