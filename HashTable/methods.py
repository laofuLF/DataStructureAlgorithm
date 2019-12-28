INITIAL_CAPACITY = 8000


# Node data structure - essentially a LinkedList node
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


# Hash table with separate chaining
class HashTable:
    # Initialize hash table
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    # Generate a hash for a given key
    # Input:  key - string
    # Output: Index from 0 to self.capacity
    def hash(self, key):
        hashsum = 0
        # For each character in the key
        for idx, c in enumerate(key):
            # Add (index + length of key) ^ (current char code)
            hashsum += (idx + len(key)) ** ord(c)
            # Perform modulus to keep hashsum in range [0, self.capacity - 1]
            hashsum = hashsum % self.capacity
        return hashsum

    # Insert a key,value pair to the hashtable
    def add(self, key):
        if self.contains(key):
            return False
        else:
            # 1. Increment size
            self.size += 1
            # 2. Compute index of key
            index = self.hash(key)
            # Go to the node corresponding to the hash
            node = self.buckets[index]
            # 3. If bucket is empty:
            if node is None:
                # Create node, add it, return
                self.buckets[index] = Node(key)
                return True
            # 4. Iterate to the end of the linked list at provided index
            prev = node
            while node is not None:
                prev = node
                node = node.next
            # Add a new node at the end of the list with provided key/value
            prev.next = Node(key)
            return True

    # Find a data value based on key
    # Input:  key - string
    # Output: value stored under "key" or None if not found
    def contains(self, key):
        # 1. Compute hash
        index = self.hash(key)
        # 2. Go to first node in list at bucket
        node = self.buckets[index]
        # 3. Traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next
        # 4. Now, node is the requested key/value pair or None
        if node is None:
            # Not found
            return False
        else:
            # Found - return the data value
            return True

