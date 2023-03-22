from data_class import *

db.connect()
admin_input = ""
print("Customer contact requests:\n")

while admin_input != "close": 
    if Ticket.select().where(Ticket.is_problem_fixed == 0).exists():
        print("Problems occured. please fix men")
        for id in Ticket.get(Ticket.is_problem_fixed == 0):
            t = Ticket.get(Ticket.is_problem_fixed == 0)
            print(t)
            print("Ticket ID: " + str(t) + " | Client: " + t.CI + " | Problem: " + t.user_input + " | Created: " + str(t.ticket_create_date))
        admin_input = input("Please choose a ticket ID to work on:\n")
    else:
        print("No Tickets available.... Refreshing in 10 seconds")
        time.sleep(10)
        

#Auswahl von Liste an Clients welche in die "clients" variable geschrieben wird

#Ping test zum client 
#rdp zum client
#info zum client