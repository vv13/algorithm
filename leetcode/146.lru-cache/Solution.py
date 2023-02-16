class Node:
    def __init__(self, value: int, key: int = -1):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        result = self.cache[key]
        self.moveToHead(result)
        return result.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.moveToHead(self.cache[key])
        else:
            if len(self.cache) + 1 > self.capacity:
                self.removeNode(self.tail.prev)
            newNode = Node(value, key)
            self.addToHead(newNode)

    def moveToHead(self, node: Node):
        self.removeNode(node)
        self.addToHead(node)

    def addToHead(self, node: Node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.cache[node.key] = node

    def removeNode(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.cache[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    obj.get(1)
    obj.put(3, 3)
    obj.get(2)
    obj.put(4, 4)
    obj.get(1)
    obj.get(3)
    obj.get(4)
