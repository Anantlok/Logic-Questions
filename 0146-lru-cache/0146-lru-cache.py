class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
class LRUCache:

    def __init__(self,capacity):
        self.capacity=capacity
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def _remove(self,node):
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node

    def _add_to_front(self,node):
        first=self.head.next
        node.next=first
        node.prev=self.head
        self.head.next=node
        first.prev=node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache)==self.capacity:
                lru=self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            new_node=Node(key,value)
            self.cache[key]=new_node
            self._add_to_front(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)