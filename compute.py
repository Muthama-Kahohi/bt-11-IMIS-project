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
from tabulate import tabulate


def compute():
	#create engine
	engine = create_engine('sqlite:///inventory.db')

	#Bind engine to Base Metadata
	Base.metadata.bind=engine

	Session = sessionmaker(bind=engine)
	session = Session()

	items=select([Items.id,Items.available_amount,Items.price])#selecting columns from Items table
	result=session.execute(items)


	items_list=[]
	
	for item in result.fetchall():
		items_list.append(item)
	
	session.close()

	items_sum=select([Items.available_amount,Items.price])#Select amount and price to calculate the total price for each item
	result_2=session.execute(items_sum)

	items_tuple=tuple(result_2)
	product_list=list(a[0]*a[1] for a in items_tuple)#returns a list of individual items and their total

	total=sum(product_list) #Sums up all the totals
	

	print(Fore.GREEN + tabulate(items_list,tablefmt="grid",headers=["Item id ","Number Available","unit price"]))
	print (Fore.RED+"TOTAL ASSET VALUE: %d"%(total))