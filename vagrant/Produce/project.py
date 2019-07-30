from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Produce, ProduceItem
app = Flask(__name__)

engine = create_engine('sqlite:///producemenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
@app.route('/produce')
def Produce():
	restaurant = session.query(Produce).first()
	items = session.query(ProduceItem).filter_by(produce_id=produce.id)
	return "This is the new Produce Function."
	
if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000)
	app.debug = True
	