import re 
import openai
import os
from peewee import *
import datetime
from dotenv import load_dotenv
import tiktoken # Debuging für die Kostenberechnung
    
request_amount = int()
enc = tiktoken.get_encoding("cl100k_base") # Kostenberechnung
db = SqliteDatabase('Tickets.db')
price=int(0)


#Database Classes 
class Ticket(Model):
    user = CharField()
    CI = CharField()
    ticket_create_date = DateTimeField(default=datetime.datetime.now)
    user_input = TextField()
    final_chat_output = TextField()
    question_rounds = IntegerField()
    is_problem_fixed = BooleanField()
    cost=IntegerField()

    class Meta:
        database = db

#General function
class functions():

    def exit():
        #function to exit program
        exit()

    def create_ticket(username, client, user_problem, answer, request_amount, state, price):
        #function to create ticket
        Ticket.create(user=username, CI=client, user_input=user_problem, final_chat_output=answer, question_rounds=request_amount, is_problem_fixed=state, cost=price)
