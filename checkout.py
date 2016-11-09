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

def check_out(itemid):
	#create engine
	engine = create_engine('sqlite:///inventory.db')

	#Bind engine to Base Metadata
	Base.metadata.bind=engine

	Session = sessionmaker(bind=engine)
	session = Session()

	item_status=session.query(Items).get(itemid)	

	#Ensures that an item is checked in before checking out
	if item_status.status:
		item_status.status=0 #Updates status to checked out	

		new_log=Logs(item_id=itemid,status=0,date=datetime.date.today())#updates log table

		session.add(new_log)
		session.commit()
		session.close()

		click.echo(Fore.GREEN+"*********************")		
		click.echo(Fore.YELLOW+"Tables updated")
		click.echo(Fore.GREEN+"*********************")
	else:
		click.echo(Fore.GREEN+"**********************************************************")
		click.echo(Fore.RED+"You cannot checkout an item that is already checked out")	
		click.echo(Fore.GREEN+"**********************************************************")
