from LinkedList import LinkedList

l = LinkedList()

l.insertEnd(12)
l.insertEnd(22)
l.insertEnd(1)
l.insertStart(43)

l.traverseList()

l.remove(22)
l.traverseList()
print(l.size())