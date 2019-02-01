import os
from dotenv import load_dotenv
env_path = '.env'
load_dotenv(dotenv_path=env_path)
from flask import Flask
from flask import jsonify
import urllib2


SHOW_MESSAGE_ROUTE = '/message'
SHOW_STATUS_ROUTE = '/status'
LINK_TO_GITHUB='https://github.com/dreckguy/decryption-challenge'
LINK_TO_DOKERHUB='https://hub.docker.com/r/dreckguy/decryption-challenge'

ENCRYPTED_FILE_ADDRESS = os.getenv("ENCRYPTED_FILE_ADDRESS")

SECRET_KEY=os.getenv('SECRET_KEY')
encryptedFile = urllib2.urlopen(ENCRYPTED_FILE_ADDRESS)
encryptedMessage = encryptedFile.readline().decode("utf-8").strip('\n')
decrypedMessage = decode(encryptedMessage,SECRET_KEY)
messageResponse = {}
messageResponse['message'] = decrypedMessage

def decode(encrypted,key): # need to write the function
    return encrypted 

app = Flask(__name__)

@app.route('/')
def showConnection():
    return "Server is up and running!\n"

@app.route(SHOW_MESSAGE_ROUTE)
def showMessage():
    
    return jsonify(messageResponse)

@app.route(SHOW_STATUS_ROUTE)
def showStatus():    
    statusResponse = {}
    statusResponse['status'] = "completed"
    statusResponse['container'] = LINK_TO_DOKERHUB
    statusResponse['project'] = LINK_TO_GITHUB
    return jsonify(statusResponse)

if __name__ == "__main__":
    app.run()




