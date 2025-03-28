class node:
    def __init__(self,data):
        self.data = data
        
class clients_list:
    def __init__(self):
      self.head = None
      
    def insert(self,data):
        new_node = node(data)

        if self.head is None:
         self.head = new_node
        return

        last_node = self.head
        while last_node.next:
         last_node = last_node.next
         last_node.next = new_node

    def print_list(self):
     current_node = self.head 
     while current_node != None:
      print(current_node.data,end=",")
     current_node = current_node.next 
    print("")

clients_list.insert(1)
clients_list.insert(2)
clients_list.insert(3)
clients_list.print_list()


    
    
        
