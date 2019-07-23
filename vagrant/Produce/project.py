from flask import Flask
app = Flask(__name__)

@app.route('/')
def Produce():
	return "This is the Produce Function."