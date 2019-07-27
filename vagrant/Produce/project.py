from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine

@app.route('/')
@app.route('/produce')
def Produce():
	return "This is the new Produce Function."
	
if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000)
	app.debug = True
	