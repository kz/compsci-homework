# Author: Kelvin Zhang
# Date Created: 2016-10-07
# Last Modified: 2016-10-16


class OrderedTree:
    def __init__(self, root_item):
        self.values = [root_item]  # The root item always goes in self.values[0]
        self.left = [None]
        self.right = [None]

    def dump(self):
        print("Values:")
        print(self.values)
        print("Left pointers:")
        print(self.left)
        print("Right pointers")
        print(self.right)

    def add_items(self, *args):
        for arg in args:
            self.add_item(arg)

    def add_item(self, item):
        # Traverse through the tree
        value_pointer = 0
        while True:
            # Check whether the value already exists in the tree
            if item == self.values[value_pointer]:
                raise ValueError("The value must not already exist in the tree")

            # Traverse down the tree or inserting a child
            # The item value is less than the current value
            if item < self.values[value_pointer]:
                # Child is not None, therefore traverse
                if self.left[value_pointer] is not None:
                    value_pointer = self.left[value_pointer]
                    continue

                # Add a child to the left
                self.values.append(item)
                self.left.append(None)
                self.right.append(None)
                self.left[value_pointer] = len(self.values) - 1
                break

            # The item value is greater than the current value
            else:
                # Child is not None, therefore traverse
                if self.right[value_pointer] is not None:
                    value_pointer = self.right[value_pointer]
                    continue

                # Add a child to the right
                self.values.append(item)
                self.left.append(None)
                self.right.append(None)
                self.right[value_pointer] = len(self.values) - 1
                break

    # Reference: https://www.tutorialspoint.com/data_structures_algorithms/tree_traversal.htm
    # left-root-right
    def print_in_order(self, pointer=0):
        # Check if the tree is empty
        if len(self.values) == 0:
            raise IndexError("The tree is empty")

        if pointer is not None:
            self.print_in_order(self.left[pointer])
            print(self.values[pointer])
            self.print_in_order(self.right[pointer])

    # root-left-right
    def print_pre_order(self, pointer=0):
        # Check if the tree is empty
        if len(self.values) == 0:
            raise IndexError("The tree is empty")

        if pointer is not None:
            print(self.values[pointer])
            self.print_pre_order(self.left[pointer])
            self.print_pre_order(self.right[pointer])

    # left-right-root
    def print_post_order(self, pointer=0):
        # Check if the tree is empty
        if len(self.values) == 0:
            raise IndexError("The tree is empty")

        if pointer is not None:
            self.print_post_order(self.left[pointer])
            print(self.values[pointer])
            self.print_post_order(self.right[pointer])

orderedTree = OrderedTree(10)
orderedTree.add_items(6, 15, 3, 7, 11, 12, 17, 100, 200)
orderedTree.dump()

# Change me!
orderedTree.print_in_order()
# orderedTree.print_pre_order()
# orderedTree.print_post_order()
