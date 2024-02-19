class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
         temp = self.head
         result = ""
         while temp is not None:
              result += str(temp.data)
              if temp.next is not None:
                  result += '-> '
              temp = temp.next
         return result
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    def __len__(self):
        return self.length

    def append(self , value):
        # time comp and space comp is o(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def inser_first(self , value):
        # time comp and space comp is o(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length +=1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length +=1
    def insert_by_index(self ,value , index):

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index -1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length +=1

    def search(self , item):
        if self.head is None:
            return False
        else:
            temp = self.head
            for i in range(self.length):
                if temp.data == item:
                    return i
                else:
                    temp = temp.next
        return -1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp.data
    def set(self , value , index):
        temp = self.head
        if index < 0 or index >= self.length:
            return None
        else:
            for _ in range(index):
                temp = temp.next
            temp.data = value
    def pop(self):
        poped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            poped_node.next = None
        self.length -=1
        return  poped_node
    def pop_right(self):
        poped_node = self.tail
        temp = self.head
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = self.tail = None
        else:
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
            self.length -=1
            return poped_node
    def remove(self , index):
        temp = self.head
        if self.head is  None:
            return None
        elif index > self.length or index < 0:
            return None
        elif index == self.length:
            return self.pop_right()
        elif index == 0:
            poped = self.head
            self.head = self.head.next
            poped.next = None
            self.length -=1
        else:
            for _ in range(index -1):
                temp = temp.next
            pre_node = temp
            removed_node = pre_node.next
            pre_node.next = removed_node.next
            removed_node.next = None
            self.length -=1
