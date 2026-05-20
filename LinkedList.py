# class Node:
#     def __init__(self):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None


# ll = LinkedList()
# ll.head = Node(5)
# second = Node(10)
# third = Node(15)
# fourth = Node(20)

# # connecting nodes
# ll.head.next = second
# second.next = third
# third.next = fourth

# # display linkedlist
# while ll.head != None:
#     print(ll.head.data, " | ", ll.head.next, " -> ", end=" ")
#     ll.head = ll.head.next


'''dynamic addition of nodes'''

import sys

class Node:
    def __init__(self, data):
        self.data = data  # instance var(5)
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, value):
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.tail.node = self.node
            self.tail = self.node

    def display(self):
        while self.head is not None:
            print(self.head.data, '|', self.head.next, '->', end=" ")
            self.head = self.head.next
        print()


if __name__ == '__main__':
    object = LinkedList()
    while True:
        print("1. Add Node Linkedlist : ")
        print("2. Add Node at beginning : ")
        print("3. Add Node in between : ")
        print("1. Add Node in End : ")
        print("5. Display Linkedlist : ")
        print("6. Exit : ")
        ch = int(input("enter your choice : "))
        if ch == 1:
            value = int(input("Enter value for node"))
            object.addNode(value)
            print("node added successfully in single linkedlist")
        elif ch == 5:
            object.display()
        elif ch == 6:
            sys.exit()
