"""
this class is a base class/interface for the implementation of any sort of binary tree

it leaves the implementation of insertion and deletion of both the node and the tree to the user,
for example, one could implement an avl tree with leaving the rest of the functions intact
"""
KEYS_ARE_EQUAL = 0
FIRST_KEY_BIGGER_THAN_SECOND_KEY = 1
FIRST_KEY_SMALLER_THAN_SECOND_KEY = -1


def compare_integers(a, b):
    if a == b:
        return KEYS_ARE_EQUAL
    elif a > b:
        return FIRST_KEY_BIGGER_THAN_SECOND_KEY
    return FIRST_KEY_SMALLER_THAN_SECOND_KEY


class Node:
    """
    a node in the tree
    """
    NO_NODE = None

    def __init__(self, parent_node, key, data, key_compare_function):
        self.parent_node = parent_node
        self.key = key
        self.data = data
        self.key_compare_function = key_compare_function
        self.height = 0

        # the larger node should be saved in the right child
        # the smaller node should be saved in the left child
        self.right = Node.NO_NODE
        self.left = Node.NO_NODE

    def insert(self, node):
        pass
        # implement as you see fit

    def delete_self(self):
        pass
        # implement as you see fit

    def get_key(self):
        return self.key

    def get_data(self):
        return self.data

    def get_small_child(self):
        return self.left

    def get_large_child(self):
        return self.right

    def get_decedent_node(self, key):
        if self.key_compare_function(key, self.key) == KEYS_ARE_EQUAL:
            return self

        elif self.key_compare_function(key, self.key) == FIRST_KEY_SMALLER_THAN_SECOND_KEY:
            small_child = self.get_small_child()
            if small_child is None:
                return None
            else:
                return small_child.get_decedent_node(key)

        else:
            large_child = self.get_large_child()
            if large_child is None:
                return None
            else:
                return large_child.get_decedent_node(key)

    @staticmethod
    def get_height_of_node(node):
        if node is None:
            return -1
        else:
            return node.height

    def update_height(self):
        self.height = max(Node.get_height_of_node(self.left),
                          Node.get_height_of_node(self.right)) + 1

    def get_min_decedent(self):
        current_decedent = self
        next_decedent = current_decedent.get_small_child()

        while next_decedent is not Node.NO_NODE:
            current_decedent = next_decedent
            next_decedent = current_decedent.get_small_child()

        return current_decedent

    def get_max_decedent(self):
        current_decedent = self
        next_decedent = current_decedent.get_large_child()

        while next_decedent is not Node.NO_NODE:
            current_decedent = next_decedent
            next_decedent = current_decedent.get_large_child()

        return current_decedent

    def get_successor_node(self):
        """
        the node with the next largest key value
        if there is no such node, the node returns itself
        """
        if self.get_large_child() is not Node.NO_NODE:
            return self.get_large_child().get_min_decedent()

        current_decedent = self
        current_parent = current_decedent.parent_node

        while current_parent is not Node.NO_NODE \
                and current_decedent is current_parent.get_large_child():
            current_decedent = current_parent
            current_parent = current_decedent.parent_node

        return current_parent


class Tree:
    def __init__(self, key_compare_function=compare_integers):
        """
        :param key_compare_function:
        the function which will be used to compare each key item from the multi_dimensional_key
        this tree search will first search the first dimension tree using the first item in the key given
        you can choose not to pass any key_compare_function but in that case you must define a < > == relation on the items
        in the keys. note that the key_compare_function passed should return the constants
        KEYS_ARE_EQUAL, FIRST_KEY_BIGGER_THAN_SECOND_KEY, FIRST_KEY_SMALLER_THAN_SECOND_KEY
        """
        self.key_compare_function = key_compare_function
        self.root_node = Node.NO_NODE

    def insert(self, key, data):
        pass
        # implement as you see fit

    def delete(self, key):
        pass
        # implement as you see fit

    def find_node_by_key(self, key):
        """
        if the node with the given key exists it returns it,
        otherwise it returns None
        """
        return self.root_node and self.root_node.get_decedent_node(key)

    def get_min_node(self):
        """
        if the tree is not empty it finds the node with the minimum key and returns it,
        otherwise it returns None
        """
        return self.root_node and self.root_node.get_min_decedent()

    def get_max_node(self):
        """
        if the tree is not empty it finds the node with the maximum key and returns it,
        otherwise it returns None
        """
        return self.root_node and self.root_node.get_max_decedent()

    def get_successor_node(self, key):
        """
        if the node with the given key exists it returns the node with the next largest key,
        otherwise it returns None
        """
        starting_node = self.find_node_by_key(key)
        return starting_node and starting_node.next_larger()
