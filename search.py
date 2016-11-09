from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import click
from colorama import init,Fore
init()
from tabulate import tabulate

#import from my dbcreate module
import declaredb
from declaredb import Items,Logs,Base

def search(search_string):
	#create engine
	engine = create_engine('sqlite:///inventory.db')

	#Bind engine to Base Metadata
	Base.metadata.bind=engine

	#creates session
	Session = sessionmaker(bind=engine)
	session = Session()

	#Selects all the items in the Items table as per given search string
	item_names=session.query(Items).filter(Items.itemname.like('%'+search_string+'%'))
	result=session.execute(item_names)

	search_list=[]
	for search in result.fetchall():
		search_list.append(search)
	if len(search_list)>0:
		print(Fore.GREEN+"--SEARCH RESULT--")
		print(Fore.WHITE + tabulate(search_list,tablefmt="grid",headers=["item_id","Name","Description","Amount_avail","price","date","status"]))
	else:
		print(Fore.RED+"No result for %s"%(search_string))
