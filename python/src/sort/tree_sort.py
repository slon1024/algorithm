def tree_sort(in_array):
    if len(in_array) < 2:
        return in_array

    tree = Tree(in_array[0])
    for i in range(1,len(in_array)):
        tree.insert(Tree(in_array[i]))

    return tree.to_array()

class Tree():
    def __init__(self, key):
        self.__key = key
        self.__left = None
        self.__right = None


    def insert(self, tree):

        if self.key > tree.key:
            self.left = tree
        else:
            self.right = tree

    def to_array(self):
        result=[]
        if self.left != None:
            result += self.left.to_array()
        result += [self.__key]
        if self.right != None:
            result += self.right.to_array()

        return result

    @property
    def key(self):
        return self.__key

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, tree):
        if self.__left == None:
            self.__left = tree
        else:
            self.__left.insert(tree)

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, tree):
        if self.__right == None:
            self.__right = tree
        else:
            self.__right.insert(tree)