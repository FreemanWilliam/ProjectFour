from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/produce')
def Produce():
	return "This is the Produce Function."