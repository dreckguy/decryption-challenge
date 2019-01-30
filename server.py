import os
from dotenv import load_dotenv
load_dotenv()
MSG = os.getenv("FLASK_APP")
print(MSG)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"