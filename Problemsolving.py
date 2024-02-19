class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
    
class linkedlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        return ""
    def append(self ,*value):
        for x in value:
            new_node = Node(x)
            if self.head is None:
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length +=1
    def remove_duplicates(self):
        # not complited
        curr = self.head
        next = curr.next
        while curr and next:
            if curr.data == next.data and next.next is None:
                curr.next = None
            elif curr.data == next.data:
                curr.next = next.next
            curr = next
            next = next.next
    def del_by_key(self , value):
        if not self.head:
            return
        elif value == self.head.data:
            curr = self.head
            self.head = self.head.next
            curr.next = None
        else:
            temp = self.head
            while temp.next.data is not value:
                temp = temp.next
            temp.next = temp.next.next
    def swap_ends(self):
        # not completed
        temp = self.head
        while temp is not self.tail:
            temp = temp.next
        self.tail.next = self.head.next
        temp.next = self.head
        self.head.next = None
        # self.head , self.tail = self.tail , self.head
    def merge_nodes(self, node):
        node.data += node.next.data
        node.next = node.next.next

    def sum_zeros(self):
        curr = self.head
        while curr.next:
            if curr.data == 0:
                while curr.next.data != 0:
                    self.merge_nodes(curr)
            curr = curr.next
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next =None
    def reverse(self):
        pre = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        self.head = pre

    def del_node(self , value):
        '''
            => try to use the solution of node.data = node.next.data
            and be award of another cases
            --> important note
            => if you want to delete the head node just press "self.head = self.head.next"
        '''
        # completed
        temp = self.head
        while temp:
            if self.head is None:
                return None
            elif self.head.data == value:
                self.head = self.head.next
            elif temp.data == value:
                curr = self.head
                while curr.next is not temp:
                    curr = curr.next
                curr.next = temp.next
            temp = temp.next
    def del_bigger(self):
        # not completed and needs some edition
        temp =self.head
        while temp.next:
            if temp.data < temp.next.data and temp.data :
                self.del_node(temp.data)
            temp = temp.next 
          
    def rotate_list(self,k):
        temp = self.head
        for _ in range(k):
            temp = temp.next
        curr = temp.next
        temp.next = None

        tail = curr
        while tail.next:
            tail =tail.next
        tail.next = self.head
        self.head = curr

first = linkedlist()
first.append(0,1,2)
first.rotate_list(2)
print(first)
