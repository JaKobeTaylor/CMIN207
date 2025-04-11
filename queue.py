from node import Node
class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def _contains_(self,target):
        traverser = self.head
        while traverser != None:
           if traverser.data.ticket == target:
              return True
           traverser = traverser.next
           return False
        def enqueue(self,data):
            new_node = Node(data)
            if self.rear == None:
             self.front = self.rear = traverser
            else: 
               self.rear.next = traverser
               self.rear = traverser
        def dequeue(self):
           if self.front == None:
              print ("Empty queue")
           else:
              traverser = self.front
              self.front = traverser.next
              return traverser.data
    def __str__(self):
       string = "First Open Ticket"
       transverser = self.front
       while transverser != None:
          string += str(transverser.data) + "\n"
          transverser = transverser.next
          string += "Last added ticket"
          return string
       
    
       