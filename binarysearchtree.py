"""
Binary Search Tree

includes BST and Node Class

"""
from recursioncounter import RecursionCounter

class Node:
    """node class to be used by Binary Search Tree"""
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.height = 0

    def is_leaf(self):
        """determines if node is leaf."""
        if self.left_child is None and self.right_child is None:
            return True
        else:
            return False

    def update_height(self):
        ''' Updates the height of the Node '''
        left_height = -1
        right_height = -1
        if self.left_child is not None:
            left_height = self.left_child.height
        if self.right_child is not None:
            right_height = self.right_child.height
        self.height = max(left_height, right_height) + 1

    def __str__(self):
        """prints string node"""
        return f"Node({self.data})"

class BinarySearchTree:
    """class for binary search tree"""
    def __init__(self):
        self.root = None

    def add(self, data):
        """adds nodes to binary search tree"""
        self.root = self.add_helper(data, self.root)

    def add_helper(self, data, cur_node):
        """Recursive add function for add"""
        RecursionCounter()

        if cur_node is None:
            return Node(data)

        if data < cur_node.data:
            cur_node.left_child = self.add_helper(data, cur_node.left_child)
        else:
            cur_node.right_child = self.add_helper(data, cur_node.right_child)

        cur_node.update_height()
        return cur_node

    def __str__(self):
        """returns string representation of tree"""
        offset = ""
        return self.print_helper(self.root, offset)

    def print_helper(self, cur_node, offset):
        """recursive function to string function"""
        RecursionCounter()
        # base case when node is None
        if cur_node is None:
            return f"{offset} [Empty]\n"
        # base case when node is leaf
        if cur_node.is_leaf():
            return f"{offset}{cur_node.data} ({cur_node.height}) [leaf]\n"
        # recursive call
        return f"{offset}{cur_node.data} ({cur_node.height})\n" + \
        self.print_helper(cur_node.left_child, offset + "    ") + \
        self.print_helper(cur_node.right_child, offset + "    ")

    def height(self):
        """to get the height"""
        if self.root is None:
            return -1
        return self.root.height

    def _height(self, cur_node, cur_height):
        """recursive part for height"""
        if cur_node is None:
            return -1
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    def find(self, value):
        """finds value in BST"""
        return self.find_helper(value, self.root)

    def find_helper(self, value, cur_node):
        """recursive find function, finds node equal to value"""
        RecursionCounter()

        if cur_node is None:
            return None

        if value == cur_node.data:
            return cur_node
        elif value < cur_node.data and cur_node.left_child is not None:
            return self.find_helper(value, cur_node.left_child)
        elif value > cur_node.data and cur_node.right_child is not None:
            return self.find_helper(value, cur_node.right_child)
        else:
            return None

    def is_empty(self):
        """determines is BST is empty"""
        if self.root is None:
            return True
        else:
            return False

    def __len__(self):
        """determins the numbers of items in BST"""
        return self.length_helper(self.root)

    def length_helper(self, curr_node):
        """recursive helper function for len()"""
        RecursionCounter()
        if curr_node is None:
            return 0
        else:
            return (self.length_helper(curr_node.left_child) + 1 + \
                self.length_helper(curr_node.right_child))

    def remove(self, data):
        """removes value from BST"""
        return self.remove_helper(self.root, data)

    def remove_helper(self, curr_node, data):
        """recursive hlper to remove()"""
        RecursionCounter()

        if curr_node.data > data:
            curr_node.left_child = self.remove_helper(curr_node.left_child, data)
        elif curr_node.data < data:
            curr_node.right_child = self.remove_helper(curr_node.right_child, data)
        else:

            # node is leaf
            if curr_node.is_leaf():
                curr_node = None

            # node has one child
            elif curr_node.right_child is None:
                return curr_node.left_child
            elif curr_node.left_child is None:
                return curr_node.right_child

            # node has two children
            else:
                pointer = curr_node.right_child
                while (pointer.left_child is not None):
                    pointer = pointer.left_child
                curr_node.data = pointer.data
                curr_node.right_child = self.remove_helper(curr_node.right_child, pointer.data)

        if curr_node is not None:
            curr_node.update_height()

        return curr_node

    def preorder(self):
        """calls recursive preorder_helper()"""
        output = []
        self.preorder_helper(self.root, output)
        return output

    def preorder_helper(self, curr_node, output):
        """Root -> Left -> Right"""
        RecursionCounter()

        if curr_node is None:
            return f"{output}"

        output.append(curr_node.data)

        self.preorder_helper(curr_node.left_child, output)
        self.preorder_helper(curr_node.right_child, output)

    def inorder(self):
        """calls recursive inorder_helper()"""
        output = []
        self.inorder_helper(self.root, output)
        return output

    def inorder_helper(self, curr_node, output):
        """left -> root -> right
        if node == null then return
        inorder(node.left)
        visit(node)
        inorder(node.right)"""

        if curr_node is None:
            return

        self.inorder_helper(curr_node.left_child, output)
        output.append(curr_node.data)
        self.inorder_helper(curr_node.right_child, output)

    def rebalance_tree(self):
        '''rebalances BST'''
        unbalanced_tree_list = self.inorder()
        for i in unbalanced_tree_list:
            self.remove(i)
        res = []

        for num in unbalanced_tree_list:
            if num in res:
                continue
            else:
                res.append(num)

        return self.re_balance_helper(unbalanced_tree_list, self)

    def re_balance_helper(self, lyst, bst):
        '''recursively rebuilds a balanced tree'''
        RecursionCounter()

        if not lyst:
            return

        mid_val = int(len(lyst) / 2)

        bst.add(lyst[mid_val])

        bst.left_child = self.re_balance_helper(lyst[0:mid_val], bst)
        bst.right_child = self.re_balance_helper(lyst[mid_val + 1:len(lyst)], bst)

        self.root.update_height()

        return bst
