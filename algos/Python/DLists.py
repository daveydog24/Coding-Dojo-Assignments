class SList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
class SLNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

list = SList()
# list.head = SLNode('Alice')
list.tail = SLNode('David')

print list.tail.value
# print list.tail.value