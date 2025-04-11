from queue import Queue
def menu():
   print("Welcome to Thibodeux's Tech Triage \n ----------------- \n")
   print(f'Type the number for the action you wish to perform and then hit Enter. \n1. Open a new ticket \n2. List All Open Tickets \n3. Close ticket\n4. Review All Closed Tickets \n5. Review Previously Closed Tickets \n6. Quit')
   response = input("What do you want to do?")
   while response != ("7"):
      if response == ("1"):
       open_tickets.enqueue("0001")
       open_tickets.enqueue("0002")
       open_tickets.enqueue("0003")
       
      print("Ticket number:", open_tickets.enqueue)
      ticket = input("Ticket: ")
      print(ticket)
      print("Ticket opened!")
      if response == ("2"):
       print("Open Tickets:")
       print(open_tickets)
      if response == ("3"):
                   closed_ticket = open_tickets.dequeue()
                   closed_tickets = closed_ticket()
                   open_tickets =  open_tickets.dequeue(closed_ticket)
                   
      if response == ("4"):
                  print(closed_ticket)
      if response == ("5"):
       print(closed_tickets)
      if response == ("6"):
           break


 