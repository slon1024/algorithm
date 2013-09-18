
class Stack:

    def __init__(self):
        self.__first = None

    def push(self, value):

        oldFirst = self.__first
        self.__first = Node(oldFirst, value)
         

    def pop(self):
        oldFirst = self.__first
        self.__first = self.__first.next_node
        return oldFirst


    def empty(self):
        return self.__first == None


class Node:
    def __init__(self, next_node, value_node):
        self.__next = next_node
        self.__value = value_node

    @property
    def __next(self):
        return self.__next


stack = Stack()
stack.push(3)
stack.push(2)

print stack.pop()
print stack.pop()

