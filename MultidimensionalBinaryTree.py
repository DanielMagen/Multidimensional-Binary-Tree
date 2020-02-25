from BaseTreeInterface import compare_integers
from AVLTree import AVLTree as BaseTree


class MultiTree:
    """
    this tree holds a multidimensional tree
    such that each piece of data is accessible by a key of length "dimensions"
    """

    def __init__(self, dimensions, key_compare_function=compare_integers):
        """
        dimensions - the number of dimensions each key is
        key_compare_function - the function which will be used to compare each key item from the multi_dimensional_key
        this tree search will first search the first dimension tree using the first item in the key given
        you can choose not to pass any key_compare_function but in that case you must implement the <= >= = relations
        on the objects in the keys
        then once it reaches a destination in the first dimension tree, this destination will be another tree that
        it will continue to search in using the second item in the key and so on
        """
        self.dimensions = dimensions
        self.key_compare_function = key_compare_function
        self.multi_tree = BaseTree(key_compare_function)
        # the base tree is a some sort of a generic binary tree
        # that inherits from the Tree class

    def insert(self, multi_dimensional_key, data):
        """
        multi_dimensional_key - a tuple containing all the keys needed
        data - the data to be inserted
        """
        current_tree = self.multi_tree

        # try to get to the lowest predefined tree you can
        i = 0
        next_tree = current_tree.find_node_by_key(multi_dimensional_key[i])
        while i < (self.dimensions - 1) and next_tree is not None:
            # self.dimensions - 1 because we want to get to the tree that will contain our data
            # if the next needed tree is None it means we have to create it so we exit this loop and go to the other one
            i += 1
            current_tree = next_tree.get_data()
            next_tree = current_tree.find_node_by_key(multi_dimensional_key[i])

        while i < self.dimensions - 1:
            # the tree is not deep enough we need to add more trees
            # we create a more tree layers until we reach the requested number of dimensions
            daughter_tree = BaseTree(self.key_compare_function)
            daughter_tree_key = multi_dimensional_key[i]
            current_tree.insert(daughter_tree_key, daughter_tree)
            current_tree = daughter_tree
            i += 1

        # we reached the tree we wanted
        current_tree.insert(multi_dimensional_key[self.dimensions - 1], data)

    def delete(self, multi_dimensional_key):
        """
        deletes and returns a node with key multi_dimensional_key if it exists from the BST.
        multi_dimensional_key - a tuple containing all the keys needed.
        should be between 1 and self.dimensions long. it does not have to be self.dimensions long

        returns - The deleted node with the given key
        """
        if len(multi_dimensional_key) < 1 or len(multi_dimensional_key) > self.dimensions:
            return None

        # first find the tree that contains the node to delete
        current_tree = self.multi_tree
        for i in range(len(multi_dimensional_key) - 1):
            current_tree = current_tree.find_node_by_key(multi_dimensional_key[i])
            if current_tree is None:
                return None
            current_tree = current_tree.get_data()

        # now delete the node
        return current_tree.delete(multi_dimensional_key[-1])

    #################### return node ####################

    def find_node_by_key(self, multi_dimensional_key):
        """
        multi_dimensional_key - a tuple self.dimensions long

        finds and returns the node with key multi_dimensional_key node
        if there is no such node it returns None
        """
        current_tree = self.multi_tree
        for i in range(self.dimensions - 1):
            current_tree = current_tree.find_node_by_key(multi_dimensional_key[i])
            if current_tree is None:
                return None
            current_tree = current_tree.get_data()
        return current_tree.find_node_by_key(multi_dimensional_key[self.dimensions - 1])

    def get_min_node(self):
        current_tree = self.multi_tree
        for i in range(self.dimensions - 1):
            current_tree = current_tree.find_min().get_data()

        return current_tree.find_min()

    def get_max_node(self):
        current_tree = self.multi_tree
        for i in range(self.dimensions - 1):
            current_tree = current_tree.find_max().get_data()

        return current_tree.find_max()

    #################### return data ####################

    def find_data_by_key(self, multi_dimensional_key):
        """
        the same as find, but instead of returning the node containing the data
        it just returns the data if it exists and None otherwise.
        of course if the data exists but is set to None it would return None either way, so it should be used carefully
        """
        result = self.find_node_by_key(multi_dimensional_key)
        if result is not None:
            return result.get_data()
        return None

    def get_min_data(self):
        """
        the same as find_min, but instead of returning the node containing the data
        it just returns the data if it exists and None otherwise.
        of course if the data exists but is set to None it would return None either way, so it should be used carefully
        """
        result = self.get_min_node()
        if result is not None:
            return result.get_data()
        return None

    def get_max_data(self):
        """
        the same as find_max, but instead of returning the node containing the data
        it just returns the data if it exists and None otherwise.
        of course if the data exists but is set to None it would return None either way, so it should be used carefully
        """
        result = self.get_max_node()
        if result is not None:
            return result.get_data()
        return None


if __name__ == "__main__":
    dimensions_of_tree = 2

    mTree = MultiTree(dimensions_of_tree)
    mTree.insert((1, 2), "hello")
    mTree.insert((1, 3), "my")
    mTree.insert((1, 4), "name")
    mTree.insert((2, 2), None)
    mTree.insert((2, 4), None)
    mTree.insert((2, 5), None)
    mTree.insert((3, 7), None)

    search = (3,)
    # print(mTree.find_data(search))
    print(mTree.multi_tree)
    mTree.delete(search)
    print(mTree.multi_tree)
