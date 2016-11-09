from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import click
from colorama import init,Fore
init()

#import from my dbcreate module
import declaredb
from declaredb import Items,Logs,Base

def additem():

	# Create an engine that stores data in the local directory
	engine = create_engine('sqlite:///inventory.db')
 
 	# Create all tables in the engine
	Base.metadata.create_all(engine)

	#Bind engine to Base Metadata
	Base.metadata.bind=engine
	item_name=input("Enter Item name: ")
	description=input("Enter a description for %s: "%(item_name))
	available_num=input("Enter the number of %s: "%(item_name))
	price=input("Enter the unit price of %s: "%(item_name))

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



