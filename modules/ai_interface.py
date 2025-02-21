from google import genai
from google.genai import types
import os
import re
import subprocess

from modules.system_info import out_info
from modules.command_executor import execute_command
from config import API_KEY

# Initialize the AI client
client = genai.Client(api_key=API_KEY)

# Function to load data from a file
def load_data(file_path):
    """Loads data from the given file if it exists."""
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = f.read()
            return data 
    else:
        return None

# Load system instructions from a file
sys_instruct = load_data("files/prompt.txt")

# Create a chat session with the AI model
chat = client.chats.create(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction=sys_instruct)
)

# Function to get AI response
def ai_response(prompt):
    """Sends a prompt to the AI model and returns the response text."""
    resp = chat.send_message(prompt)
    return resp.text

# Function to remove emojis and asterisks from text
def remove_emojis_and_stars(text):
    """Removes all emojis and asterisks (*) from the given text."""
    text = re.sub(r"[\U00010000-\U0010FFFF]", "", text)  # Remove emojis
    text = re.sub(r"\*", "", text)  # Remove asterisks
    return text.strip()

# Function to process special commands in AI responses
def process_special_commands(response):
    """Processes special commands in AI responses, such as system info or command execution."""
    system_response = None
    command_output = None

    # Clean the response from emojis and asterisks
    response = remove_emojis_and_stars(response)

    # Handle system info request
    if "%%система%%" in response:
        system_response = out_info()
        response = re.sub(r"%%система%%", "", response).strip()

    # Handle command execution
    command_match = re.search(r"!!(.*?)!!", response)
    if command_match:
        command = command_match.group(1)
        response = re.sub(r"!!.*?!!", "", response).strip()
        execute_command(command)

    return response, None
