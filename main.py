from SingleLinkedList import SingleLinkedList

ll = SingleLinkedList()
ll.append(15)
ll.append(17)
ll.append(123)
ll.append(33)
ll.push_front(10)
ll.push_index(44, 5)
print(ll.length())
ll.out()
ll.push_index(19, 3)
print(ll.length())
ll.out()
