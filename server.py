import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask
import urllib
ENCRYPTED_FILE_ADDRESS = os.getenv("ENCRYPTED_FILE_ADDRESS")
encryptedFile = urllib.request.urlopen(ENCRYPTED_FILE_ADDRESS)
encryptedText = encryptedFile.readline()

app = Flask(__name__)
@app.route("/")
def hello():
    return encryptedText