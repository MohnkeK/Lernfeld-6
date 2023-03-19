# Chatbot zum einfachen Kommunizieren mit den Kunden. 
import re 
import openai
import os

openai.organization = os.getenv("OPENAI_ORG")
openai.api_key = os.getenv("OPENAI_KEY")


print("Moin, \nsie schreiben nun mit dem Chatbot, er wird ihnen nun weiterhelfen.\nSollten sie das Programm beenden wollen schreiben sie einfach 'bye'.\n")

username = input("What is your Username?\n")
if username == "bye": 
    print("Well Bye then")


client = input("Whats you Clients name?\n")

while client != "bye" and client == "" or not bool(re.search("[cC]\d\d\d\d", client)): 
    client = input("No Client found\nWhats your Clients name?\n")

if client == "bye":
    print("Well Bye then")

user_question = input("What seems to be your Problem?\n")

while user_question != "" and user_question != "bye" and user_question != "fixed":
    #Fragen Loop für Kunden
    response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=user_question,
            temperature=0.6,)
    answer = response['choices'][0]['text']
    print(answer)
    user_question = input("If your question was answered and your problem was fixed please write 'fixed'\nIf your question was not fixed please try asking in a different way.\n")