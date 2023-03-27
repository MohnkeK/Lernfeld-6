from data_class import *

db.connect()
admin_input = ""
ticket_list = []
print("Customer contact requests:\n")

while admin_input != "close":
    if Ticket.select().where(Ticket.is_problem_fixed == 0).exists():
        print("Problems occured. please fix men")
        query = Ticket.select().where(Ticket.is_problem_fixed == 0)
        for entry in query:
            print("Ticket ID: " + str(entry) + " | Client: " + entry.CI + " | Problem: " +
                  entry.user_input + " | Created: " + str(entry.ticket_create_date))
        admin_input = input("Please choose a ticket ID to work on:\n")

        while admin_input != "close" and admin_input != "" and admin_input != "4" and admin_input != "refresh":
            entry = Ticket.get(Ticket.id == admin_input)
            client = entry.CI
            print("Ticket ID: " + str(entry) + " | Client: " + entry.CI + " | Problem: " + entry.user_input +
                  " | Answer: " + entry.final_chat_output + " | Created: " + str(entry.ticket_create_date) + "\n")
            
            while admin_input != "close" and admin_input != "" and admin_input != "4":
                admin_input = input("Please choose your option: \n1: Test ping to Client\n2: Remote connect to client\n3: Show Client information\n4: Mark ticket as resolved\n")
                # ping test
                # rdp
                # general info
                if admin_input == "1":
                    print("No Ping available\n")
                elif admin_input == "2":
                    print("Function not set yet\n")
                elif admin_input == "3":
                    print("Client Information unavailable\n")
                elif admin_input == "4":
                    update = Ticket.update({Ticket.is_problem_fixed: True}).where(Ticket.id == str(entry))
                    update.execute()
                    print("Ticket was marked as resolved\n")

        if admin_input == "close":
            print("Have a nice day.\n")
            exit()    
        os.system('cls||clear')
    else:
        print("No Tickets available.... Refreshing in 10 seconds")
        time.sleep(10)

print("Goodbye")
