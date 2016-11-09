from sqlalchemy import create_engine,update
from sqlalchemy.orm import sessionmaker
import datetime
import click
from colorama import init,Fore
init()
from sqlalchemy.sql import select,text
import declaredb
from declaredb import Items,Logs,Base
import datetime

def check_in(itemid):
	#create engine
	engine = create_engine('sqlite:///inventory.db')

	#Bind engine to Base Metadata
	Base.metadata.bind=engine

	Session = sessionmaker(bind=engine)
	session = Session()

	item_status=session.query(Items).get(itemid)

	#Ensures that item is previously checked out before checking in
	if item_status.status:
		click.echo(Fore.GREEN+"***********************************************************")
		click.echo(Fore.RED+"You cannot check in an item that has not been checked out")
		click.echo(Fore.GREEN+"**********************************************************")

	else:
		item_status.status=1 #updates status to checked in 			
		new_log=Logs(item_id=itemid,status=1,date=datetime.date.today()) #updates the log table
		session.add(new_log)
		session.commit()
		session.close()

		click.echo(Fore.GREEN+"*********************")		
		click.echo(Fore.YELLOW+"Tables updated")
		click.echo(Fore.GREEN+"*********************")
		
