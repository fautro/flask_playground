from flask import Flask as F

app = F(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'