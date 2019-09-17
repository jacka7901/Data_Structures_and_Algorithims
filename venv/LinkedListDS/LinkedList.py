from Node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.counter = 0

    def insertStart(self, data):
        self.counter += 1
        newNode = Node(data)
        #if there is no nodes in the LinkedList make this the head
        if not self.head:
            self.head = newNode
        #sets the new node to the new head and the current head to the next node
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size(self):
        return self.counter

    def insertEnd(self, data):

        if self.head is None:
            self.insertStart(data)
            return

        self.counter +=1

        newNode = Node(data)
        actualNode = self.head

        # starting from the head and going all the way to the last node
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        #setting the next node of the last node in the list to the new node
        actualNode.nextNode = newNode

    def remove(self, data):
        self.counter -=1
        #if there is at least 1 element in the list
        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.remove(data, self.head)


    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print('%d ' % actualNode.data)
            actualNode = actualNode.nextNode