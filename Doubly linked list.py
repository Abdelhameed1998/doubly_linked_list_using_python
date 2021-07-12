class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList():
    def __init__(self, headnode=None, tailnode=None):
        self.headnode = headnode
        self.tailnode = tailnode
        self.count = 0
        if headnode:
            self.count = 1
        if tailnode:
            self.count = 1
        if self.tailnode and self.headnode:
            self.insert_first(self.headnode)
            self.insert_last(self.tailnode)


    def insert(self, new_node, position):
        current = self.headnode
        counter = 1
        if position == 1:
            new_node.next = self.headnode
            self.headnode.prev = new_node
            self.headnode = new_node
            self.count += 1

        if position - self.count == 1:
            self.tailnode.next = new_node
            new_node.prev = self.tailnode
            self.tailnode = new_node
            self.count += 1

        else:
            while counter < position and current:
                if counter == position - 1:
                    new_node.next = current.next
                    new_node.prev = current

                    current.next = new_node
                    current.next.prev = new_node
                    self.count +=1

                current = current.next
                counter += 1


    def append_front(self, new_node): ## means on the top or last
        current = self.headnode
        if self.headnode:  ## check if headnode not None
            while current.next:  # start from head node until reach last node
                current = current.next
            current.next = new_node
            ## last node added is the tail node
            new_node.prev = current
            current.next = new_node
            self.tailnode = new_node
        else:
            ## first element is head and tail at the same time
            self.headnode = new_node
            self.tailnode = new_node
            self.headnode.prev = None
        self.count += 1

    def print_linked_list(self):
        current = self.headnode
        while current.next:
            print(current.value)
            current = current.next
        print(current.value)

    def insert_first(self, new_element): # means at the back or bottom
        new_element.next = self.headnode
        self.headnode.prev = new_element
        self.headnode = new_element
        self.count +=1

    def insert_last(self, new_element): # means at the front or top
        self.tailnode.next = new_element
        new_element.prev = self.tailnode
        self.tailnode = new_element
        self.count +=1


    def delete_first(self):
        if self.headnode:
            deleted_element = self.headnode
            temp = deleted_element.next
            self.headnode = temp
            return deleted_element
        else:
            return None


bll = DoublyLinkedList()
bll.append_front(Node(1))
bll.append_front(Node(2))

# bll.append_front(Node(3))
# bll.insert_first(Node(5))
# bll.insert_last(Node(4))

bll.insert(Node(0),6)
print("count",bll.count)
# bll.insert(Node(4), 5)

bll.print_linked_list()
