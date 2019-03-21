class SLNode(object):
 def __init__(self, value):
  self.value = value
  self.next = None

class SList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def PrintAllVals(self):
        runner = self.head
        while(runner.next != None):
            print(runner.value)
            runner = runner.next
        print runner.value # last value

    def AddBack(self, value):
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = SLNode(value)
    
    def AddFront(self, value):
        new_head = SLNode(value)
        temp_head = self.head
        temp_value = temp_head.value
        temp_next = temp_head.next
        self.head = new_head
        new_head.next = temp_head

    def InsertBefore(self, nextValue, value):
        runner = self.head
        # loops through to find a node before the value searched
        while(runner.next.value != nextValue):
            runner = runner.next

        A = runner
        C = runner.next
        B = SLNode(value)
        temp = C
        runner.next = B
        B.next = C

    def InsertAfter(self, preValue, value):
        runner = self.head
        while (runner.value != preValue):
            runner = runner.next
        
        A = runner
        C = runner.next
        B = SLNode(value)
        A.next = B
        B.next = C

    def RemoveNode(self, value):
        runner = self.head
        while (runner.next.value != value):
            runner = runner.next
        runner.next = runner.next.next

    def ReverseList(self):
        runner = self.head
        arr = []
        count = 0
        while (runner.next != None):
            arr.append(runner.value)
            runner = runner.next
            count += 1
        list.head = SLNode(runner.value)
        count -= 1
        runner = list.head

        while (count >= 0):
            runner.next = SLNode(arr[count])
            runner = runner.next
            count -= 1
        runner.next = None
        return self
            

list = SList()
list.head = SLNode('Alice')
list.head.next = SLNode('Chad')
list.head.next.next = SLNode('Debra')
list.AddBack('Kim')
list.AddFront('David')
list.InsertBefore('Debra', 'Geoff')
list.InsertAfter('Kim', 'Grandma')
list.RemoveNode('Geoff')
list.PrintAllVals()
print ""
list.ReverseList()
list.PrintAllVals()