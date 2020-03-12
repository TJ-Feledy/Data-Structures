"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next




"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None and self.tail is None:
            return 'empty'
        curr_node = self.head
        output = ''
        output += f'({curr_node.value}) <-> '
        while curr_node.next is not None:
            curr_node = curr_node.next
            output += f'({curr_node.value}) <-> '
        return output

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #  adding to an empty list
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            # create new node
            self.head = new_node
            self.tail = new_node
        else:
            # adding a new value, to existing list
            # link new_node with current head
            new_node.next = self.head
            self.head.prev = new_node
            # update head
            self.head = new_node
            


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #  if list is empty
        if self.head is None and self.tail is None:
            return
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        else:
            # have more than one element
            value = self.head.next
            next_head = self.head.next
            next_head.prev = None
            self.head.next = None
            self.head = next_head
            self.length -= 1
            return value


    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        #  adding to an empty list
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            # create new node
            self.head = new_node
            self.tail = new_node
        else:
            # adding a new value, to existing list
            # link new_node with current tail
            new_node.prev = self.tail
            self.tail.next = new_node
            # update tail
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        #  if list is empty
        if self.head is None and self.tail is None:
            return
        # if list has only one element
        elif self.tail == self.head:
            # unlink the node
            value = self.tail.value
            self.tail = None
            self.head = None
            return value
        else:
            # have more than one element
            value = self.tail.prev
            prev_tail = self.tail.prev
            prev_tail.next = None
            self.tail.prev = None
            self.tail = prev_tail
            self.length -= 1
            return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # if list is empty
        if self.head is None and self.tail is None:
            return
        else:
            # change current node's prev and next to point at eachother
            # save the init_head
            # change curr_node to head and link with init_head
            curr_node = node
            init_head = self.head
            right = curr_node.next
            left = curr_node.prev

            right.prev = left
            left.next = right

            self.head = curr_node

            curr_node.next = init_head
            curr_node.prev = None
            init_head.prev = curr_node




    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # if list is empty
        if self.head is None and self.tail is None:
            return
        else:
            # change current node's prev and next to point at eachother
            # save the init_tail
            # change curr_node to tail and link with init_tail
            curr_node = node
            init_tail = self.tail
            right = curr_node.next
            left = curr_node.prev

            right.prev = left
            left.next = right

            self.tail = curr_node

            curr_node.next = None
            curr_node.prev = init_tail
            init_tail.next = curr_node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        #  if list is empty
        if self.head is None and self.tail is None:
            return
        elif node == self.head:
            # if deleted node is head
            # make the next node the head and adjust the links
            # set curr_nodes pointers to none
            curr_node = node
            next_head = curr_node.next
            
            next_head.prev = None
            self.head = next_head

            curr_node.next = None

            self.length -= 1
            
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass
