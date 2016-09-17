# Author: Kelvin Zhang
# Date Created: 2016-09-09
# Last Modified: 2016-09-15

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


class AlphabeticalLinkedList:
    def __init__(self, length: int):
        self.start = None
        self.length = length
        self.nodes = [None for _ in range(0, length)]

    def dump(self):
        """
        Outputs all nodes in the linked list, along with its length and starting index
        """
        print("Length: {!s}".format(self.length))
        print("Starting index: {!s}".format(self.start))
        print([[i, x.get_item(), x.get_pointer()] if x is not None else None for i, x in enumerate(self.nodes)])

    def add(self, new_node: Node):
        """
        Adds a node to the linked list in alphabetical order
        :param new_node: Node
        :return:
        """

        if None not in self.nodes:
            raise IndexError("The linked list is full")

        # Find a random empty array position to insert the node into
        new_node_location = None
        while True:
            new_node_location = random.randint(0, self.length - 1)
            if self.nodes[new_node_location] is None:
                break
        self.nodes[new_node_location] = new_node

        # Set the location to self.start if LinkedList has not been added to yet
        if self.start is None:
            self.start = new_node_location
            new_node.set_pointer(None)
            return

        # If the linked list is not empty, traverse the linked list
        # and find the first instance where current_node > new_node
        next_location = self.start
        current_node = self.nodes[next_location]
        while True:
            # Handle inserting the item to the start of the linked_list
            if next_location == self.start and current_node.get_item() > new_node.get_item():
                new_node.set_pointer(self.start)
                self.start = new_node_location
                return new_node_location

            # Handle reaching the end of the linked list (i.e., item is "zzz...")
            if current_node.get_pointer() is None:
                current_node.set_pointer(new_node_location)
                new_node.set_pointer(None)
                return new_node_location

            if current_node.get_item() > new_node.get_item():
                new_node.set_pointer(current_node.get_pointer())
                current_node.set_pointer(new_node_location)
                return new_node_location

            next_location = current_node.get_pointer()
            current_node = self.nodes[next_location]

    def search(self, item):
        """
        Searches for the first occurrence of an item in the linked list
        and prints the node's position and pointer.
        Raises ValueError if a node with the matching item is not found.
        :except ValueError
        :param item
        :return:
        """

        # Ensure that the linked list has at least one node
        if self.start is None:
            raise ValueError("The linked list has not been given a starting node")

        # Traverse through the linked list, comparing items
        position = 1
        next_location = self.start
        while next_location is not None:
            current_node = self.nodes[next_location]

            # Compare the items to see if they match
            if current_node.get_item() == item:
                # Item found
                print("Node found - Order in list: {!s} - Pointer to node: {!s}".format(position, next_location))
                return

            # Check if the end of the linked list has been reached without success
            if current_node.get_pointer() is None:
                raise ValueError("Item not found in list")

            # Set the next location
            position += 1
            next_location = current_node.get_pointer()

    def delete(self, item):
        """
        Deletes the first node which has an item matching with the item parameter.
        Raises ValueError if a node with the matching item is not found.
        :except ValueError
        :param item
        :return:
        """

        # Ensure that the linked list has at least one node
        if self.start is None:
            raise ValueError("The linked list has not been given a starting node")

        # Traverse through the linked list, comparing items
        next_location = self.start
        previous_node = None
        while True:
            current_node = self.nodes[next_location]

            # Compare the items to see if they match
            if current_node.get_item() == item:

                # Handle deletion of the start of the list
                if previous_node is None:
                    old_start = self.start
                    if current_node.get_pointer is None:
                        self.start = None
                    else:
                        self.start = current_node.get_pointer()
                    self.nodes[old_start] = None
                    return

                # Handle deletion of all other cases
                previous_node.set_pointer(current_node.get_pointer())
                self.nodes[next_location] = None
                return

            # Check if the end of the linked list has been reached without success
            if next_location is None:
                raise ValueError("Item not found in list")

            # Set the next location
            previous_node = current_node
            next_location = current_node.get_pointer()


linkedList = AlphabeticalLinkedList(5)
linkedList.add(Node('A'))
linkedList.add(Node('B'))
linkedList.add(Node('C'))
linkedList.add(Node('D'))
linkedList.add(Node('E'))
linkedList.dump()
print("=========")
linkedList.search("A")
linkedList.search("B")
linkedList.search("C")
linkedList.search("D")
linkedList.search("E")
print("=========")
linkedList.delete("A")
linkedList.delete("B")
linkedList.delete("D")
linkedList.dump()
print("=========")
linkedList.add(Node('A'))
linkedList.dump()
