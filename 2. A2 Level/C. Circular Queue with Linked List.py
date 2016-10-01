# Author: Kelvin Zhang
# Date Created: 2016-09-20
# Last Modified: 2016-10-01

import random


class Node:
    def __init__(self, item):
        self.item = item
        self.pointer = None

    def get_item(self):
        return self.item

    def get_pointer(self):
        return self.pointer

    def set_item(self, item):
        self.item = item

    def set_pointer(self, pointer):
        self.pointer = pointer


class CircularQueue:
    def __init__(self, length: int):
        self.head = None
        self.tail = None
        self.length = length
        self.nodes = [None for _ in range(0, length)]

        # Populate all nodes to form a circle of pointers
        previous_node_location = None
        for i in range(0, length):
            # Find a random, empty node location
            while True:
                new_node_location = random.randint(0, self.length - 1)
                if self.nodes[new_node_location] is None:
                    break

            # Add an empty node at this location
            self.nodes[new_node_location] = Node(None)

            # Assign the pointer for the previous node
            if previous_node_location is not None:
                self.nodes[previous_node_location].set_pointer(new_node_location)
            else:
                # Set the head if this node is the first one
                self.head = new_node_location

            # Assign the pointer for the last node if applicable
            if i == length - 1:
                self.nodes[new_node_location].set_pointer(self.head)

            previous_node_location = new_node_location

    def dump(self):
        """
        Outputs all nodes in the linked list, along with its length and starting index
        """
        print("Length: {!s}".format(self.length))
        print("Head: {!s}".format(self.head))
        print("Tail: {!s}".format(self.tail))
        print([[i, x.get_item(), x.get_pointer()] if x is not None else None for i, x in enumerate(self.nodes)])

    def add(self, item):
        """
        Adds a node to the linked list in alphabetical order
        :param item
        :return:
        """

        # Check whether the circular queue is full
        # The queue is full if the tail is just before the head
        if self.tail is not None and self.nodes[self.tail].get_pointer() == self.head:
            raise IndexError("The circular queue is full")

        # Increment the tail
        # If the tail is set to None, the the head is assigned to the tail
        if self.tail is None:
            self.tail = self.head
        else:
            self.tail = self.nodes[self.tail].get_pointer()

        # Assign the item to the node at the tail
        self.nodes[self.tail].set_item(item)

    def pop(self):
        """
        Pops the node at the head
        :return: Node
        """

        # Ensure that the linked list has at least one node
        if self.head is None:
            raise ValueError("The linked list has not been given a starting node")

        # Update head and tail locations
        old_head_pointer = self.head
        if old_head_pointer == self.tail:
            # Only one node in the queue
            self.head = None
            self.tail = None
        else:
            # Set head location to next in queue
            self.head = self.nodes[old_head_pointer].get_pointer()

        # Clear the node at the old head
        old_item = self.nodes[old_head_pointer].get_item()
        self.nodes[old_head_pointer].set_item(None)

        return old_item


linkedList = CircularQueue(5)
linkedList.add('A')
linkedList.add('B')
linkedList.add('C')
linkedList.add('D')
linkedList.add('E')
linkedList.dump()
print('===============')
print(linkedList.pop())
print(linkedList.pop())
linkedList.dump()
print('===============')
linkedList.add('F')
linkedList.add('G')
linkedList.dump()