class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        self.pre = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
        result = ""
        temp = self.head
        for _ in range(self.length):
            result += str(temp.data)
            if temp.next is not None:
                result += ' <-> '
            temp = temp.next
        return result

    def append(self , value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.pre = self.tail
            self.tail = new_node
        self.length +=1
    def prepend(self ,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.pre = new_node
            self.head = new_node
        self.length +=1
    def travers(self):
        temp =  self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
    def reverse_traverse(self):
        temp = self.tail
        while temp is not None:
            print(temp.data)
            temp = temp.pre
    def search(self , value):
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False
    def get(self , index):
        if index < 0 or index > self.length:
            return None
        if index < self.length // 2:
            temp = self.head
            for _ in range( index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1 , index , -1):
                temp = temp.pre
        return temp
    def set(self , index , value):
        node = self.get(index)
        if node:
            node.data = value
            return True
        return False
    def insert(self , index , value):
        if index > self.length or self.length <0:
            return None
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index -1)
            new_node.next = temp.next
            new_node.pre = temp
            temp.next.pre = new_node
            temp.next = new_node
        self.length +=1
    def pop_first(self):
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.pre = None
        self.length -=1
    def pop(self):
        if self.length == 0:
            return None
        elif self.length ==1:
            self.head = self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.pre
            temp.pre = None
            self.tail.next = None
        self.length -=1
    def remove(self , index):
        removed = self.get(index)
        if self.head is None:
            return None
        elif index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            removed.pre.next = removed.next
            removed.next.pre = removed.pre
            removed.next = None
            removed.pre = None
            self.length -=1
    def clear(self):
        self.head = None
        self.tail = None
        self.length =0
first = DLL()
first.prepend(10)
first.prepend(20)
first.prepend(30)
print(first)
first.remove(2)
print(first)
