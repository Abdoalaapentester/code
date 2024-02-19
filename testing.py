class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_nodes_with_key(head, key):
    # Create a dummy node to simplify code
    dummy = ListNode(next=head)
    current = dummy

    # Traverse the list and remove nodes with the specified key
    while current.next is not None:
        if current.next.value == key:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next
