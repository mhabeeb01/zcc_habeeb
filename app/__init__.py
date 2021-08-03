from flask import Flask
app = Flask(__name__)

from dotenv import load_dotenv 
import os
load_dotenv()
def secrets():
    user = os.getenv("EMAIL")
    return f"{user}"
def secretspwd():
    pwd = os.getenv("TOKEN")
    return f"{pwd}"
from app import routes