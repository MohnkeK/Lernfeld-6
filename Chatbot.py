# Chatbot zum einfachen Kommunizieren mit den Kunden. 
from data_class import *
load_dotenv()


db.connect()
db.create_tables([Ticket])
openai.organization = os.getenv("OPENAI_ORG")
openai.api_key = os.getenv("OPENAI_KEY")

print("Moin, \nyou're now writing with a Chatbot, he will assist you now.\nIncase you want to exit the Program please just write 'bye'.\n")

username = input("What is your Username?\n")
# LDAP Check if Username is in Domain or Database check 
if username == "bye": 
    print("Well Bye then")
    exit()

client = input("Whats you Clients name?\n")
# Check if client is in Database/Domain 
while client != "bye" and client == "" or not bool(re.search("^[cC]\d\d\d\d$", client)): 
    client = input("No Client found\nWhats your Clients name?\n")

if client == "bye":
    print("Well Bye then")
    exit()

user_question = input("What seems to be your Problem?\n")
user_problem=user_question
user_question_split = user_question.split()

while user_question != "" and user_question != "bye" and user_question != "fixed" and request_amount != 3 and functions.keyword_check(user_question_split) == True:
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt="only answer if this question is technical: " + user_question,
            max_tokens=256,
            temperature=0.6)
    
    answer = response['choices'][0]['text']
    quser_question_split = user_question.split()
    question_length = int(len(user_question_split))
    request_amount = request_amount+1
    price = price + len(enc.encode(answer))+question_length 

    print(answer)
    user_problem=user_question
    user_question = input("\nIf your question was answered and your problem was fixed please write 'fixed'\nIf your problem was not fixed please try asking in a different way.\n")
    user_question_split = user_question.split()

if request_amount>=3:
    print("You reached the end of the rainbow, we will create a Ticket for you now.\nA professional will contact you as soon as possible.")
    state=bool(False)
    functions.create_ticket(username, client, user_problem, answer, request_amount, state, price)
    exit()

elif user_question == "bye":
    print("Well by then")
    state=bool(False)
    functions.create_ticket(username, client, user_problem, answer, request_amount, state, price)
    exit()

elif user_question == "fixed":
    print("Thanks for your cooperation")
    state=bool(True)
    functions.create_ticket(username, client, user_problem, answer, request_amount, state, price)
    exit()

elif functions.keyword_check(user_question_split) == False:
    print("Please dont missuse this chatbot and only ask a technical question.\nThank you this session will now be closed.")
    functions.create_ticket(username, client, user_problem, answer, request_amount, state, price)
    exit()