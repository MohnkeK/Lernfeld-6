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
        while admin_input != "close" and admin_input != "":
            print(admin_input)
            entry = Ticket.get(Ticket.id == admin_input)
            client = entry.CI
            print("Ticket ID: " + str(entry) + " | Client: " + entry.CI + " | Problem: " + entry.user_input +
                  " | Answer: " + entry.final_chat_output + " | Created: " + str(entry.ticket_create_date) + "\n")
            admin_input = input("Please choose your option: \n")
            # ping test
            # rdp
            # general info

    else:
        print("No Tickets available.... Refreshing in 10 seconds")
        time.sleep(10)

print("Goodbye")
