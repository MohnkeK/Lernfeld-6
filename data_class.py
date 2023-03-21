import re 
import openai
import os
from dotenv import load_dotenv
import tiktoken # Debuging für die Kostenberechnung

#Exit function
class bfunctions():

    def exit():
        exit()
    """Function to exit the program per Button"""
    