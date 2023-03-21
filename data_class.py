import re 
import openai
import os
from peewee import *
import datetime
from dotenv import load_dotenv
import tiktoken # Debuging für die Kostenberechnung

#Exit function
class functions():

    def exit():
        exit()
    """Function to exit the program per Button"""
    
db = SqliteDatabase('Tickets.db')

#Database Classes 
class Ticket(Model):
    username = CharField()
    client = CharField()
    sessionstart = DateTimeField(default=datetime.datetime.now)
    user_question = TextField()
    final_answer = TextField()
    question_rounds = IntegerField()
    is_problem_fixed = BooleanField()
    session_end = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
