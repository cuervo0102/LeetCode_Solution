class Node: 
    def __init__(self, key, value) -> None:
        self.key = key 
        self.value = value
        self.previous = None 
        self.next = next 



class LRUCache():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)  # add the dummy node to not check every time if a node head or tail and won't to check if the lidt is empty or not
        self.tail = Node(0, 0)  
        self.head.next = self.tail
        self.tail.previous = self.head


    def insert_head(self, node):
        node.next = self.head.next 
        node.previous = self.head
        self.head.next.previous = node
        self.head.next = node


    
    def remove_node(self, node):
        node.previous.next = node.next
        node.next.previous = node.next


    def remove_tail(self):
        tail_prev = self.tail.previous
        self.remove_node(tail_prev)
        del self.cache[tail_prev.key]



    def move_to_head(self, node):
        self.remove_node(node)
        self.insert_head(node)


    def put(self, key, value):
        if key in self.cache: 
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else: 
            if len(self.cache) >= self.capacity:
                self.remove_tail()

            new_node = Node(key, value)
            self.insert_head(new_node)
            self.cache[key] = new_node


    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            return node.value
        
        return -1



























