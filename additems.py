from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import click
from colorama import init,Fore
init()
from termcolor import colored

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

	if len(item_name)>0:#Ensures that data is added as item name
		try:
			description=input("Enter a description for %s: "%(item_name))
			available_num=int(input("Enter the number of %s: "%(item_name)))
			price=int (input("Enter the unit price of %s: "%(item_name)))

			if isinstance(available_num,int) and isinstance(price,int):#Ensures that the available_num and price are integers
			
				if len(description)!=0 and available_num!=None and price!=None:#Esures that the three variables are not empty

					#creates session
					cur_session=sessionmaker(bind=engine)
					session=cur_session()

					#Statement to insert items to table
					new_item=Items(itemname=item_name,description=description,available_amount=available_num,price=price,date_added=datetime.datetime.now(),status=1)
					
					#executes statement
					session.add(new_item)
					session.commit()

					#Feedback when successfull
					print(Fore.GREEN+ "*********************")
					print(Fore.RED+ "Item successfully added")
					print(Fore.GREEN+ "*********************")

				else:
					print(Fore.GREEN+ "*********************************")
					print(Fore.RED+ "All items have to be filled")
			else:
				print(Fore.GREEN+ "*********************************")
				print(Fore.RED+ "Invalid types")
				
		except ValueError as e:
			print(Fore.GREEN+ "****************************************************")
			print(colored("Enter integers for number of items and price","red"))
					
					

	else:
		print(Fore.GREEN+ "***********************************")
		print(Fore.RED+ "Item name cannot be blank")






