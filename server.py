import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from flask import jsonify

import urllib
ENCRYPTED_FILE_ADDRESS = os.getenv("ENCRYPTED_FILE_ADDRESS")
encryptedFile = urllib.request.urlopen(ENCRYPTED_FILE_ADDRESS)
encryptedMessage = encryptedFile.readline()

messageResponse = {'temperature':'24.3'}

statusResponse = "status"

SHOW_MESSAGE_ROUTE = os.getenv("SHOW_MESSAGE_ROUTE")
SHOW_STATUS_ROUTE = os.getenv("SHOW_STATUS_ROUTE")

app = Flask(__name__)
@app.route(SHOW_MESSAGE_ROUTE)
def showMessage():
    return jsonify(messageResponse)
@app.route(SHOW_STATUS_ROUTE)
def showStatus():
    return statusResponse




