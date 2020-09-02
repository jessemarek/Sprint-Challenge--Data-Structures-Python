"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value < Node's value
        if value < self.value:
            # we need to go left
            # if we see that there is no left child,
            if self.left is None:
                # then we can wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there is a child
            else:
                # call the left child's `insert` method
                self.left.insert(value)
        # otherwise, value >= Node's value
        else:
            # we need to go right
            # if we see there is no right child,
            if self.right is None:
                # then we can wrap the value in a BSTNode and park it
                self.right = BSTNode(value)
            # otherwise there is a child
            else:
                # call the right child's `insert` method
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if target value is equal to value
        if self.value == target:
            return True
        # if target is not equal to value check if we have a left or right
        # child and compare target to value to see which path to take
        # if target is < value take the left path
        elif self.left and target < self.value:
            return self.left.contains(target)
        # if target is > value take the right path
        elif self.right and target > self.value:
            return self.right.contains(target)
        # if there are no children and target != value then return False
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # check if node has a right child
        if self.right:
            # if there is a right child execute that node's get_max
            return self.right.get_max()
        # if no right child, this node is the greatest value in the BST
        return self.value
        """ # create a variable to store the current node
        current = self

        # if the current node has a right child
        # set current to the right child
        while current.right is not None:
            current = current.right

        # once we reach the right most leaf it will have
        # the greatest value that exists in the tree.
        # return that node's value
        return current.value """

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # execute callback fn on self
        fn(self.value)

        # if left child exisits...
        if self.left is not None:
            # pass the callback to the child
            self.left.for_each(fn)

        # if right child exisits...
        if self.right is not None:
            # pass the callback to the child
            self.right.for_each(fn)

    # Part 2 -----------------------

    #     1
    #      \
    #       8
    #      /
    #     5
    #    / \
    #   3   7
    #  / \ /
    # 2  4 6

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # left -> node -> right

        # dive down to the left most leaf
        # this will be the smallest value
        if node.left:
            node.left.in_order_print(node.left)

        # if no other left children exist this means
        # the current node is now the smallest value
        # that hasn't yet been handled. print the value
        print(node.value)

        # if the node has a right child then we have values
        # that are greater than the current node. print that value
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # node -> left -> right
        from collections import deque

        # create a queue and pass it the first node
        queue = deque()
        queue.append(node)

        # continue to traverse while there are nodes in the queue
        while len(queue) > 0:
            current = queue.popleft()

            # if the next level has a left node...
            if current.left:
                # add to queue
                queue.append(current.left)

            # if the next level has a right node...
            if current.right:
                # add to queue
                queue.append(current.right)

            # print the current node's value
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # node -> left -> right OR node -> right -> left
        from collections import deque

        # create a queue and pass it the first node
        queue = deque()
        queue.append(node)

        # continue to traverse while there are nodes in the queue
        while len(queue) > 0:
            # get first node in queue
            current = queue.popleft()

            # print current node's value
            print(current.value)

            # if current node has a left child,
            # execute that child's dft_print()
            if(current.left):
                current.left.dft_print(current.left)

            # if current node has a right child,
            # execute that child's dft_print()
            if(current.right):
                current.right.dft_print(current.right)

        # Stretch Goals -------------------------
        # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # node -> left -> right
        self.dft_print(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # left -> right -> node

        # if node has a left child,
        # execute that child's post_order_dft()
        if(node.left):
            node.left.post_order_dft(node.left)

        # if node node has a right child,
        # execute that child's post_order_dft()
        if(node.right):
            node.right.post_order_dft(node.right)

        # print node's value
        print(node.value)
