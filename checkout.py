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
from termcolor import colored

def check_out(item_id):
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
					item_status.status=0 #Updates status to checked out	

					new_log=Logs(item_id=itemid,status=0,date=datetime.datetime.now())#updates log table

					session.add(new_log)
					session.commit()
					session.close()

					click.echo(Fore.GREEN+"*********************")		
					click.echo(Fore.YELLOW+"Item Checked out")
					print(colored("*********************","green"))

				else:
					click.echo(Fore.GREEN+"**********************************************************")
					click.echo(Fore.RED+"You cannot check out an item has been  checked out")	
					print(colored("******************************************************************","green"))

			else:
				click.echo(Fore.GREEN+"**********************************************************")
				click.echo(Fore.RED+"No such item in database.")
				print(colored("******************************************************************","green"))

		else:
			click.echo(Fore.GREEN+"**********************************************************")
			print(colored("Item id has to be a number","green"))
			
	except ValueError as e:
		click.echo(Fore.GREEN+"**********************************************************")
		print(colored("Invalid value. Please enter a number","red"))		
	
