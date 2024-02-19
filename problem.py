print (123)
class Node:
    def __init__(self ,value= None , next = None):
        self.data = value
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        return ""
    def append(self , *value):
        for x in value:
            new_node = Node(x)
            if self.head is None:
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length +=1
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
    def get(self , index):
        if self.head is None:
            return None
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            return temp.data
    def set(self , index , value):
        node = self.get(index)
        node.data = value
    def pop_right(self):
        if self.head is None:
            return None
        else:
            self.head = self.head.next
    def pop(self):
        curr = self.head
        while curr.next is not self.tail:
            curr = curr.next
        poped = self.tail
        self.tail = curr
        curr.next = None
        return poped
    def remove_node(self , value):
        if self.head.data == value:
            self.head = self.head.next
        elif self.tail.data == value:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
        else:
            curr = self.head
            while curr.next.data is not value:
                curr = curr.next
            curr.next = curr.next.next
        self.length -=1

    def partly_reverse(self , right , left):
        # not completed
        pre = None
        curr = self.head
        for _ in range(left - 1):
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
    def remove_zero(self):
        # there is a problme in big test
        pre = self.head
        curr = pre.next
        while curr:
            if pre.data + curr.data != 0:
                pre = curr
                curr = curr.next
            else:
                temp = self.head
                while temp.next is not pre:
                    temp = temp.next
                pre = temp
                pre.next = curr.next
                curr = curr.next
    def double_it(self):
        temp = self.head
        numbers = ""
        while temp:
            numbers += str(temp.data)
            temp = temp.next
        final = int(numbers) * 2
        final_result = list(str(final))
        dummy = Node()
        curr = dummy
        for x in final_result:
            curr.next = Node(x)
            curr = curr.next
    def counter(self , value):
        count = 0
        temp = self.head
        while temp:
            if temp.data == value:
                count +=1
            temp = temp.next
        return count
    def remove_all_repeated(self):
        # not completed
        pre = self.head
        curr = pre.next
        while curr:
            if pre.data == curr.data:
                self.remove_node(pre.data)
                self.remove_node(curr.data)
                curr = curr.next.next
                pre = pre.next.next
            else:
                pre = curr
                curr = curr.next
    def get_middle(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.data
    def calc(self):
        temp = self.head
        counter = 0
        while temp:
            counter +=1
            temp = temp.next
        if counter % 2 == 0:
            return (counter / 2) -1
        else:
            return counter //2
    def size(self):
        counter = 0
        temp = self.head
        while temp:
            counter +=1
            temp = temp.next
        return counter
    def reorder_list(self):
        # we need a method to pop last node => done
        # we need to get the middle of the linked list to stop then it => done
        # we need a method to know the number the nodes => done
        
        curr = self.head
        for _ in range(int(self.calc())):
            poped = self.pop()
            poped.next = curr.next
            curr.next = poped
            curr = curr.next.next
    def swapnodes(self):
        ...
first = linkedlist()

