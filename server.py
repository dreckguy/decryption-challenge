import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask
import urllib
ENCRYPTED_FILE_ADDRESS = os.getenv("ENCRYPTED_FILE_ADDRESS")
encryptedFile = urllib.request.urlopen(ENCRYPTED_FILE_ADDRESS)
for line in encryptedFile:
    print(line)




app = Flask(__name__)
@app.route("/")
def hello():
    return ENCRYPTED_FILE_ADDRESS