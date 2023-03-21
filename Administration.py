from data_class import *


db.connect()
if Ticket.select().where(Ticket.is_problem_fixed == 0).exists():
    print("Problems occured. please fix men")
 
#Suche nach Probelemen die nicht gefixed wurden
#Auswahl von Liste an Clients welche in die "clients" variable geschrieben wird

#Ping test zum client 
#rdp zum client
#info zum client