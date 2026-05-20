# import sys


# class Queue:
#     def __init__(self, size):
#         self.myQueue = []
#         self.queueSize = size

#     def isFull(self):
#         if len(self.myQueue) == size:
#             return True
#         else:
#             return False

#     def display(self):
#         print(self.myQueue)

#     def Enqueue(self, value):
#         if self.isFull():
#             print("Queue is full")
#         else:
#             self.myQueue.append(value)
#             print("element inserted")

#     def isEmpty(self):
#         if self.myQueue == []:
#             return True
#         else:
#             return False

#     def delete(self):
#         if self.isEmpty():
#             print("queue is Empty")
#         else:
#             self.myQueue.pop(0)

#     def peek(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             print("Fist element is :", self.myQueue[0])

#     def DeleteQueue(self):
#         del self.myQueue
#         print("Queue Deleted")
#         # self.myQueue=None


# size = int(input("enter the size of queue : "))
# obj = Queue(size)
# print("Queue is created")
# while True:
#     print("1. Enqueue Operation")
#     print("2. Display Queue")
#     print("3. Delete Operation")
#     print("4. Peek Operation")
#     print("5. Delete Queue")
#     print("6. Exit")
#     choice = int(input("enter your choice: "))
#     if choice == 1:
#         value = int(input("enter value to insert: "))
#         obj.Enqueue(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.delete()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.DeleteQueue()
#     elif choice == 6:
#         sys.exit()


# NOTE
''' 
Stack using List
EASY  TO iMPLEMENT
SPEED PROBLEM WHEN IT GROWS

Stack using Linked List
-- fast performance 
-- Implementation is not easy


Queue using list
-- easy to implement
--- speed problem when it grows

Queue using Linked List
-- fast performance 
-- Implementation is not easy

'''


fruit = {}


def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1


addone('Apple')
addone('Banana')
addone('apple')
print(len(fruit))
# o/p = 3
