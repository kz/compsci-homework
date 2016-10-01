# Author: Kelvin Zhang
# Date Created: 2016-09-26
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


class StackLinkedList:
    def __init__(self, length: int):
        self.top_pointer = None
        self.length = length
        self.nodes = [None for _ in range(0, length)]

    def dump(self):
        """
        Outputs all nodes in the linked list, along with its length and starting index
        """
        print("Length: {!s}".format(self.length))
        print("Top of stack pointer: {!s}".format(self.top_pointer))
        print([[i, x.get_item(), x.get_pointer()] if x is not None else None for i, x in enumerate(self.nodes)])

    def add(self, item):
        """
        Adds a node to the linked list in alphabetical order
        :param item
        :return:
        """

        if None not in self.nodes:
            raise IndexError("The stack is full")

        # Find a new location in the array to insert a new node with the item into
        new_node_location = None
        while True:
            new_node_location = random.randint(0, self.length - 1)
            # Check whether there is an existent node at new_node_location
            if self.nodes[new_node_location] is None:
                self.nodes[new_node_location] = Node(item)
                break

        # Set the pointer to the next node if applicable
        if self.top_pointer is not None:
            self.nodes[new_node_location].set_pointer(self.top_pointer)
        else:
            self.nodes[new_node_location].set_pointer(None)
        self.top_pointer = new_node_location

    def pop(self):
        """
        Pops the first node
        :return: Node
        """

        # Ensure that the linked list has at least one node
        if self.top_pointer is None:
            raise ValueError("The linked list has not been given a starting node")

        # Take a copy of the pointer to the current top of stack
        old_top_pointer = self.top_pointer

        # Change the top pointer to the next item in stack
        self.top_pointer = self.nodes[old_top_pointer].get_pointer()

        # Delete the old top
        popped_node = self.nodes[old_top_pointer]
        self.nodes[old_top_pointer] = None

        # Return the old node
        return popped_node


linkedList = StackLinkedList(5)
linkedList.add("1")
linkedList.add("2")
linkedList.add("3")
linkedList.add("4")
linkedList.add("5")
linkedList.dump()

print(linkedList.pop().get_item())
