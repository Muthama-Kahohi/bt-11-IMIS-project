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

def check_in(item_id):
	#create engine
	engine = create_engine('sqlite:///inventory.db')

	#Bind engine to Base Metadata
	Base.metadata.bind=engine

	Session = sessionmaker(bind=engine)
	session = Session()
	try:
		itemid=int(item_id)

		if isinstance(itemid,int):


			id=session.query(Items.id)
			id_list=[]
			flag=False

			for index in id:
				id_list.append(list(index))

			for index in id_list:
				if itemid in index:
					flag=True
					break

			if flag:#Ensures that the item is in the database

				item_status=session.query(Items).get(itemid)	

				#Ensures that an item is checked out before checking in
				if item_status.status:
					click.echo(Fore.GREEN+"**********************************************************")
					click.echo(Fore.RED+"You cannot check in an item has not been previously checked out")	
					click.echo(Fore.GREEN+"**********************************************************")

				else:
					item_status.status=1 #Updates status to checked out	

					new_log=Logs(item_id=itemid,status=1,date=datetime.datetime.now())#updates log table

					session.add(new_log)
					session.commit()
					session.close()

					click.echo(Fore.GREEN+"*********************")		
					click.echo(Fore.YELLOW+"Item Checked in")
					click.echo(Fore.GREEN+"*********************")
			else:
				click.echo(Fore.GREEN+"**********************************************************")
				click.echo(Fore.RED+"No such item in database.")
				click.echo(Fore.GREEN+"**********************************************************")		
		else:
			click.echo(Fore.GREEN+"**********************************************************")
			click.echo(Fore.RED+"Item id has to be a number")
	except ValueError as e:
		click.echo(Fore.GREEN+"**********************************************************")
		click.echo(Fore.RED+"Invalid value. Please enter a number")		


					
		
