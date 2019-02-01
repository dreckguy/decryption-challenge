import os
#from dotenv import load_dotenv
#load_dotenv()
from flask import Flask
from flask import jsonify
import urllib



SHOW_MESSAGE_ROUTE = os.getenv("SHOW_MESSAGE_ROUTE")
SHOW_STATUS_ROUTE = os.getenv("SHOW_STATUS_ROUTE")


app = Flask(__name__)
@app.route('/')
def showConnection():
    return "Server is up and running!\n"
@app.route(SHOW_MESSAGE_ROUTE)
def showMessage():
    ENCRYPTED_FILE_ADDRESS = os.getenv("ENCRYPTED_FILE_ADDRESS")
    encryptedFile = urllib.request.urlopen(ENCRYPTED_FILE_ADDRESS)
    encryptedMessage = encryptedFile.readline().decode("utf-8").strip('\n')
    messageResponse = {}
    messageResponse['message'] = encryptedMessage
    return jsonify(messageResponse)

@app.route(SHOW_STATUS_ROUTE)
def showStatus():
    LINK_TO_GITHUB = os.getenv("LINK_TO_GITHUB")
    LINK_TO_DOKERHUB = os.getenv("LINK_TO_DOKERHUB")
    
    statusResponse = {}
    statusResponse['status'] = "completed"
    statusResponse['container'] = LINK_TO_DOKERHUB
    statusResponse['project'] = LINK_TO_GITHUB
    return jsonify(statusResponse)

if __name__ == "__main__":
    app.run()




