class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def pop(self):
        temp = self.head
        if temp == None:
            return None

        self.head = self.head.next
        if self.head != None:
            self.head.prev = None

        self.size -= 1
        return temp.val

    def append(self, val):
        newNode = Node(val)

        if self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail

        self.tail = newNode
        self.size += 1
        return newNode

    def moveToEnd(self, node):
        if node == None:
            return

        prev = node.prev
        next = node.next

        # XNX - just connect the two
        # NX - head = X
        # XN - nothing changes
        # N - nothing changes

        if prev != None and next != None:
            # Close the gap
            prev.next = next
            next.prev = prev
            # Stick node on end
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
        elif prev == None and next != None:
            # Make next the new head
            self.head = next
            next.prev = None
            # Stick node on end
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node


class LRUCache:

    def __init__(self, capacity: int):
        self.queue = LinkedList()
        self.values = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not self.values.__contains__(key):
            return -1
        keyNode, value = self.values.get(key)
        self.queue.moveToEnd(keyNode)
        return value

    def put(self, key: int, value: int) -> None:
        if self.values.__contains__(key):
            keyNode, oldValue = self.values.get(key)
            self.values[key] = (keyNode, value)
            self.queue. moveToEnd(keyNode)
        else:
            if self.queue.size >= self.capacity:
                oldKey = self.queue.pop()
                self.values.pop(oldKey)

            keyNode = self.queue.append(key)
            self.values[key] = (keyNode, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
