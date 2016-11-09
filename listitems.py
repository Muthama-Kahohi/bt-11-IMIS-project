from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select,text
import datetime
import click
from colorama import init,Fore
init()
#import from my dbcreate module
import declaredb
from declaredb import Items,Logs,Base
from tabulate import tabulate

def listitems():
	#create engine
	engine = create_engine('sqlite:///inventory.db')

	#Bind engine to Base Metadata
	Base.metadata.bind=engine

	#creates session
	Session = sessionmaker(bind=engine)
	session = Session()

	#Selects all the items in the Items table
	items=select([Items])
	result=session.execute(items)

	items_list=[]

	#orders the result to enable  tabulation
	for item in result.fetchall():
		items_list.append(item)
	session.close()

	if len(items_list)>0:
		print(Fore.GREEN + tabulate(items_list,tablefmt="grid",headers=["item_id","Name","Description","Amount_avail","price","date","status"]))
	else:
		print ("Table empty")		
	

	
