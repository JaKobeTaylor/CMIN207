class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)

    
        if self.head is None:
         self.head = new_node
        else:
           last_node = self.head
           while last_node.next:
              last_node = last_node.next

              last_node.next = new_node
            
        def print_list(self):
           if self.head is None:
              print("I'm sorry that is not an allowed action.")
              return
           current_node = self.head
        while True:
            print(last_node.data,end=",")
            last_node = last_node.next
            if last_node == self.head:
               break
            print()
            LinkedList.insert(1)
            LinkedList.insert(2)
            LinkedList.insert(3)
            LinkedList.insert(4)
            LinkedList.insert(5)


              