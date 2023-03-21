# Chatbot zum einfachen Kommunizieren mit den Kunden. 
from data_class import *
load_dotenv()


db.connect()
db.create_tables([Ticket])
start=datetime.datetime.now
openai.organization = os.getenv("OPENAI_ORG")
openai.api_key = os.getenv("OPENAI_KEY")

print("Moin, \nyou're now writing with a Chatbot, he will assist you now.\nIncase you want to exit the Program please just write 'bye'.\n")

username = input("What is your Username?\n")
if username == "bye": 
    print("Well Bye then")
    exit()
#Username in Datenbank einfügen

client = input("Whats you Clients name?\n")

while client != "bye" and client == "" or not bool(re.search("^[cC]\d\d\d\d$", client)): 
    client = input("No Client found\nWhats your Clients name?\n")

if client == "bye":
    print("Well Bye then")
    exit()

#Client in Datenbank einfügen

user_question = input("What seems to be your Problem?\n")

while user_question != "" and user_question != "bye" and user_question != "fixed" and request_amount != 3:
    #Keyword whitelist
    #Fragen in Datenbank mit einfügen 
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt="only answer if this question is technical: " + user_question,
            max_tokens=256,
            temperature=0.6)
    
    answer = response['choices'][0]['text']
    #Antwort in Datenbank mit einfügen

    #Berechnung der Token (1000t=0.02€)
    question_split = user_question.split()
    question_length = int(len(question_split))
    request_amount = request_amount+1
    print(len(enc.encode(answer))+question_length) # Print Token amount

    print(answer)
    user_question = input("\nIf your question was answered and your problem was fixed please write 'fixed'\nIf your problem was not fixed please try asking in a different way.\n")

if request_amount>=3:
    print("You reached the end of the rainbow, we will create a Ticket for you now.\nA professional will contact you as soon as possible.")
    state=bool(False)
    end=datetime.datetime.now
    functions.create_ticket(username, client, start, user_question, answer, request_amount, state, end)

elif user_question == "bye":
    print("Well by then")
    state=bool(False)
    end=datetime.datetime.now
    functions.create_ticket(username, client, start, user_question, answer, request_amount, state, end)
    exit()

elif user_question == "fixed":
    print("Thanks for your cooperation")
    state=bool(True)
    end=datetime.datetime.now
    functions.create_ticket(username, client, start, user_question, answer, request_amount, state, end)
    exit()