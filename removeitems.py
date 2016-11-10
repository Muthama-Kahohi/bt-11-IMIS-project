from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import click
from colorama import init,Fore
init()


#import from my dbcreate module
import declaredb
from declaredb import Items,Logs,Base
from termcolor import colored

def remove(itemid):
	#create engine
	engine = create_engine('sqlite:///inventory.db')

	#Bind engine to Base Metadata
	Base.metadata.bind=engine

	Session = sessionmaker(bind=engine)
	session = Session()
	try:
		id=session.query(Items).get(itemid)		
		if id==None:
			print (colored("**********************","green"))
			print(colored("No such item in db","red"))
			print(colored("************************","green"))
		else:
			id_found=id.id
			if int(id_found)==int(itemid):#ensures that item to be removed is in database	
				item_id=int(itemid)
				#Query to delete item as per item id
				
				delete_this=session.query(Items).filter(Items.id == item_id).first()
				session.delete(delete_this)
				session.commit()

				#feedback to user
				click.echo(Fore.GREEN+ "***********************")
				click.echo(Fore.RED+"Item successfully removed")
				print(colored("***********************","green"))
			else:
				click.echo(Fore.GREEN+"**********************************************************")
				click.echo(Fore.RED+"No such item in database.")
				print(colored("**********************************************************","green"))
		
	
	except ValueError as e:
		click.echo(Fore.GREEN+"**********************************************************")
		print(colored("Invalid value. Please enter a number","green"))	

	