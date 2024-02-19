class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def __str__(self):
        return str(self.data)


class cslinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        result = ""
        temp = self.head
        for _ in range(self.length):
            result += str(temp.data) + " "
            temp = temp.next
        return result

    def inser_first(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1

    def insert_by_index(self, value, index):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        elif index < 0 or index > self.length:
            raise Exception("out of range")
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1

    def travers(self):
        temp = self.head
        for _ in range(self.length):
            print(temp.data)
            temp = temp.next

    def search(self, value):
        temp = self.head
        for i in range(self.length):
            if temp.data == value:
                return i
            else:
                temp = temp.next
        return None

    def get(self, index):
        if index > self.length or index < 0:
            raise Exception("out of range")
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        if index > self.length or index < 0:
            raise Exception("out of range")
        temp = self.get(index)
        if temp is not None:
            temp.data = str(value)
            return True
        return False

    def pop_first(self):
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            poped_node = self.head
            self.head = self.head.next
            poped_node.next = None
            self.tail.next = self.head
        self.length -= 1

    def pop(self):
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp is not self.tail:
                temp = temp.next
            self.tail.next = None
            self.tail = temp
            self.tail.next = self.head
        self.length -= 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            # poped = self.head
            # self.head = self.head.next
            # poped.next = None
            # self.tail.next = self.head
            return self.pop_first()
        elif index == self.length:
            return self.pop()
        else:
            pre_node = self.get(index-1)
            removed = pre_node.next
            pre_node.next = removed.next
            removed.next = None
        self.length -=1

    def clear(self):
        if self.length == 0:
            return None
        else:
            self.tail.next = None
            self.head = None
            self.tail = None
            self.length = 0
first = cslinkedlist()
first.append(10)
first.append(20)
first.append(30)
first.remove(0)
print(first)
