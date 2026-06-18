class LRUCache:
    class ListNode:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None


    def __init__(self, capacity: int):
        self.is_present = {}
        self.size = 0
        self.capacity = capacity

        self.head = LRUCache.ListNode(0,0)
        self.tail = LRUCache.ListNode(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head


    def add_node(self, node):
        from_node = node.prev
        to_node = node.next
        from_node.next = to_node
        to_node.prev = from_node
    

    def add_node_back(self, node):
        prev_of_tail = self.tail.prev
        prev_of_tail.next = node
        node.prev = prev_of_tail
        node.next = self.tail
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key in self.is_present:
            node = self.is_present[key]
            val = node.val

            # Assign the prev and next nodes for the current node which we skipped.
            self.add_node(node)

            # Assign the node we remove to the tail.
            self.add_node_back(node)

            return val
        
        return -1


    def put(self, key: int, value: int) -> None:
        
        # If key already present, then get the key and put it in the back.
        if key in self.is_present:
            node = self.is_present[key]
            self.add_node(node)
        
        new_node = LRUCache.ListNode(key, value)
        self.is_present[key] = new_node
        self.add_node_back(new_node)

        if len(self.is_present) > self.capacity:
            node_to_delete = self.head.next
            self.add_node(node_to_delete)
            del self.is_present[node_to_delete.key]
        
        return

"""
class LRUCache:

    def __init__(self, capacity: int):
        self.is_present = {}
        self.q = deque([])
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.is_present:

            # First delete it from the queue.
            for i in range(len(self.q)):
                if self.q[i] == key:
                    del self.q[i]
                    break
            
            val = self.is_present[key]
            self.q.append(key)
            return val

        return -1


    def put(self, key: int, value: int) -> None:

        # If the size is full, no matter waht we need to delete it first.
        # Then populate what's left.
        if self.size == self.capacity:

            # Two cases, either the element is already in the queue then update it and put back in queue.
            # If not in queue then pop it and push it by popping from front.

            if key in self.is_present:

                # Find and delete the entry from queue if present and then push back.
                for i in range(len(self.q)):
                    if self.q[i] == key:
                        del self.q[i]
                        del self.is_present[key]
                        break
            
            else:
                # If key not present then pop the front of the key 
                pop_key = self.q.popleft()
                del self.is_present[pop_key]
            
            self.size -= 1
        
        else:

            # Now if the size is not yet full then we have two situations.
            # First if the element is present then we find and delete it from position and arrange the position.
            # If element is not present directly push back.

            if key in self.is_present:

                for i in range(len(self.q)):
                    if self.q[i] == key:
                        del self.q[i]
                        del self.is_present[key]
                        self.size -= 1
                        break
        
        self.is_present[key] = value
        self.size += 1
        self.q.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
