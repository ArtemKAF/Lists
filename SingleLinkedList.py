from SNode import Node


class SingleLinkedList(object):

    def __init__(self):
        self.head = None

    def length(self):
        count = 0
        if self.head:
            cur_node = self.head
            while cur_node:
                cur_node = cur_node.get_next()
                count += 1
        return count

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if not cur_node:
            self.head = new_node
            return
        while cur_node.get_next():
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def push_front(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def push_index(self, data, index):
        if index == 0:
            self.push_front(data)
            return
        if self.length() == index:
            self.append(data)
            return
        count = 1
        cur_node = self.head
        while count != index:
            cur_node = cur_node.get_next()
            count += 1
        new_node = Node(data)
        new_node.set_next(cur_node.get_next())
        cur_node.set_next(new_node)

    def out(self):
        cur_node = self.head
        if not cur_node:
            print("List is Empty")
            return
        while cur_node:
            print(cur_node.get_data())
            cur_node = cur_node.get_next()
