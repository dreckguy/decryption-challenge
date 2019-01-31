import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from flask import jsonify
import urllib
ENCRYPTED_FILE_ADDRESS = os.getenv("ENCRYPTED_FILE_ADDRESS")
encryptedFile = urllib.request.urlopen(ENCRYPTED_FILE_ADDRESS)
encryptedMessage = encryptedFile.readline().decode("utf-8").strip('\n')
print(encryptedMessage)


LINK_TO_GITHUB = os.getenv("LINK_TO_GITHUB")
LINK_TO_DOKERHUB = os.getenv("LINK_TO_DOKERHUB")


statusResponse = {}
statusResponse['status'] = "completed"
statusResponse['container'] = LINK_TO_DOKERHUB
statusResponse['project'] = LINK_TO_GITHUB

messageResponse = {}
messageResponse['message'] = encryptedMessage

SHOW_MESSAGE_ROUTE = os.getenv("SHOW_MESSAGE_ROUTE")
SHOW_STATUS_ROUTE = os.getenv("SHOW_STATUS_ROUTE")


app = Flask(__name__)
#CORS(app)
@app.route('/')
def showConnection():
    return "Server is up and running!"
@app.route(SHOW_MESSAGE_ROUTE)
def showMessage():
    return jsonify(messageResponse)

@app.route(SHOW_STATUS_ROUTE)
def showStatus():
    return jsonify(statusResponse)




