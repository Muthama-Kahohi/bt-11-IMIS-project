from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import click
from colorama import init,Fore
init()

#import from my dbcreate module
import declaredb
from declaredb import Items,Logs,Base

def remove(itemid):
	#create engine
	engine = create_engine('sqlite:///inventory.db')

	#Bind engine to Base Metadata
	Base.metadata.bind=engine

	Session = sessionmaker(bind=engine)
	session = Session()

	try:
		item_id=int(itemid)
		#Query to delete item as per item id
		delete_this=session.query(Items).filter(Items.id == item_id).first()
		session.delete(delete_this)
		session.commit()

		#feedback to user
		click.echo(Fore.GREEN+ "***********************")
		click.echo(Fore.RED+"Item successfully removed")
		click.echo(Fore.GREEN+ "***********************")
	except ValueError as e:
		click.echo(Fore.GREEN+"**********************************************************")
		click.echo(Fore.RED+"Invalid value. Please enter a number")		