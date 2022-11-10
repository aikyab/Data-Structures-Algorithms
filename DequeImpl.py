
class DNode:
    def __init__(self, val=0):
        self.prev = None
        self.next = None
        self.val = val


class Deque:
    def __init__(self):
        self.head, self.tail = DNode(), DNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, value):
        new_node = DNode(val=value)
        last = self.tail.prev
        last.next = new_node
        new_node.prev = last
        new_node.next = self.tail
        self.tail.prev = new_node

    def append_left(self, value):
        # head <-> 1 <-> tail
        new_node = DNode(val=value)
        res = self.head.next
        new_node.next = res
        new_node.prev = self.head
        self.head.next = new_node
        res.prev = new_node
    
    def pop(self):
        last = self.tail.prev
        second_last = last.prev
        second_last.next = self.tail
        self.tail.prev = second_last
        return last.val
    
    def popleft(self):
        first = self.head.next
        second_node = first.next
        self.head.next = second_node
        second_node.prev = self.head
        return first.val
    
q = Deque()
q.append(1)
q.append(2)
q.append_left(3)
print(q.popleft())
