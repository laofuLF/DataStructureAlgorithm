class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to test if the data is in the set
    def contains(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.data == data:
                found = True
                return True
            else:
                current = current.next
        if current is None:
            return False
        return False

    # Function to add data to the set if it's not already there
    def add(self, new_data):
        if not self.contains(new_data):
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node
            return True
        return False

    # Function to return the size of the set
    def size(self):
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.next
        return count

