# Chatbot zum einfachen Kommunizieren mit den Kunden. 
import re 

print("Moin, \nsie schreiben nun mit dem Chatbot, er wird ihnen nun weiterhelfen.\nSollten sie das Programm beenden wollen schreiben sie einfach 'bye'.\n")

username = input("What is your Username?\n")
if username == "bye": 
    print("Well Bye then")


client = input("Whats you Clients name?\n")

while client != "bye" and client == "" or not bool(re.search("[cC]\d\d\d\d", client)): 
    client = input("No Client found\nWhats your Clients name?\n")

if client == "bye":
    print("Well Bye then")

user_question = input("What seems to be your Problem?")

while user_question != "" and user_question != "bye":
    #Fragen Loop für Kunden