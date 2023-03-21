from data_class import *

db.connect()
if Ticket.select().where(Ticket.is_problem_fixed == 0).exists():
    print("Problems occured. please fix men")
    t = Ticket.get(Ticket.is_problem_fixed == 0)
    print("Ticket ID: " + "Client" + t.CI + "Problem: " + t.user_input + "Created: " + t.ticket_create_date)
    


#Auswahl von Liste an Clients welche in die "clients" variable geschrieben wird

#Ping test zum client 
#rdp zum client
#info zum client