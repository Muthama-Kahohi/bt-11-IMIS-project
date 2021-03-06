from sqlalchemy import create_engine,update
from sqlalchemy.orm import sessionmaker
import datetime
from colorama import init,Fore
init()
from sqlalchemy.sql import select,text
import declaredb
from declaredb import Items,Logs,Base
import datetime
import click
from tabulate import tabulate
from sqlalchemy.sql import select,text
from termcolor import colored



def view(item_id):
	print(Fore.YELLOW+"Display two tables of Item id: "+item_id)
	print(Fore.RED+"****ITEM DETAILS")
	

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
					
				item_details=session.query(Items).get(itemid)
				log_details=select([Logs]).where(Logs.item_id==itemid)
				result=session.execute(log_details)

				log_list=[]

				for log in result.fetchall():
					log_list.append(log)

				session.close

				item_data=[item_details.id,item_details.itemname,item_details.description,item_details.available_amount,item_details.price,item_details.date_added,item_details.status]
				details=[item_data]

				print(Fore.CYAN + tabulate(details,tablefmt="grid",headers=["item_id","Name","Description","Amount_avail","price","date","status"]))
				print(Fore.GREEN+"******************************************************************************************************************")
				print(Fore.RED+"****LOG DETAILS")
				print(colored(tabulate(log_list,tablefmt="grid",headers=["id","item_id","status","Date"]),"green"))
				print(colored("True == checked in","yellow"))
				print(colored("False== checked out","yellow"))


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
	

	