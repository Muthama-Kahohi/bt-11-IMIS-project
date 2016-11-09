from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import click
from colorama import init,Fore
init()

#import from my dbcreate module
import declaredb
from declaredb import Items,Logs,Base

def additem(item_name,description,available_num,price):

	# Create an engine that stores data in the local directory
	engine = create_engine('sqlite:///inventory.db')
 
 	# Create all tables in the engine
	Base.metadata.create_all(engine)

	#Bind engine to Base Metadata
	Base.metadata.bind=engine

	#creates session
	cur_session=sessionmaker(bind=engine)
	session=cur_session()

	#Statement to insert items to table
	new_item=Items(itemname=item_name,description=description,available_amount=available_num,price=price,date_added=datetime.date.today(),status=1)
	
	#executes statement
	session.add(new_item)
	session.commit()

	#Feedback when successfull
	click.echo(Fore.GREEN+ "*********************")
	click.echo(Fore.RED+ "Item successfully added")
	click.echo(Fore.GREEN+ "*********************")



