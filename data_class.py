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


#Database Classes 
class Ticket(Model):
    user = CharField()
    CI = CharField()
    sessionstart = CharField()
    user_input = TextField()
    final_chat_output = TextField()
    question_rounds = IntegerField()
    is_problem_fixed = BooleanField()
    session_end = CharField()

    class Meta:
        database = db

#General function
class functions():

    def exit():
        #function to exit program
        exit()

    def create_ticket(username, client, start, user_question, answer, request_amount, state, end):
        #function to create ticket
        Ticket.create(user=username, CI=client,sessionstart=start, user_input=user_question, final_chat_output=answer, question_rounds=request_amount, is_problem_fixed=state, session_end=end)
