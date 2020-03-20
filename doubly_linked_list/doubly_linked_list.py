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
        output += f'head = {self.head.value}, tail = {self.tail.value}'
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
            self.length -= 1
            return value
        else:
            # have more than one element
            value = self.head.value
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
            self.length -= 1
            return value
        else:
            # have more than one element
            value = self.tail.value
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
            self.delete(node)
            self.add_to_head(node.value)



    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # if list is empty
        if self.head is None and self.tail is None:
            return
        else:
            self.delete(node)
            self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        #  if list is empty
        if self.head is None and self.tail is None:
            return

        elif self.head == self.tail:
            # if only one node
            self.head = None
            self.tail = None

            self.length -= 1

            return node

        elif self.head.value == node or self.head.value == node.value:
            # if deleted node is head
            # make the next node the head and adjust the links
            # set curr_nodes pointers to none
            curr_node = self.head
            next_head = curr_node.next
            
            next_head.prev = None
            self.head = next_head

            curr_node.next = None

            self.length -= 1

            return node

        elif self.tail.value == node or self.tail.value == node.value:
            # if deleted node is tail
            # make the next node the tail and adjust the links
            # set curr_nodes pointers to none
            curr_node = self.tail
            next_tail = curr_node.prev
            
            next_tail.next = None
            self.tail = next_tail

            curr_node.prev = None

            self.length -= 1

            return node

        else:
            # deleted is between head & tail
            curr_node = self.head

            while curr_node.next is not None:
                if curr_node.value == node:
                    value = curr_node.value
                    right = curr_node.next
                    left = curr_node.prev

                    right.prev = left
                    left.next = right

                    curr_node.next = None
                    curr_node.prev = None

                    return value
                else:
                    curr_node = curr_node.next
            
            self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None and self.tail is None:
            return 'empty'

        curr_node = self.head
        val_list = []

        if self.head == self.tail:
            val_list = [self.head.value]

        while curr_node is not None:
            val_list.append(curr_node.value)
            curr_node = curr_node.next

        return max(val_list)
        

our_dll = DoublyLinkedList()

# our_dll.add_to_tail(5)
# our_dll.add_to_head(10)
# our_dll.add_to_tail(0)
# our_dll.delete(our_dll.head)
# our_dll.delete(our_dll.head)
# our_dll.add_to_tail(50)

# print(our_dll)
# print(our_dll.get_max())