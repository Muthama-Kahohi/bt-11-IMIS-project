#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    imis (-i | --interactive)
    imis (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
  
"""

import sys
import csv
import cmd
import sqlite3
from docopt import docopt, DocoptExit
from colorama import init,Fore
init()
from pyfiglet import Figlet

#import my modules
from declaredb import Items,Logs,Base
from additems import additem
from listitems import listitems
from removeitems import remove
from checkin import check_in
from checkout import check_out
from view import view
from search import search
from compute import compute


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class ImisInteract (cmd.Cmd):
    f = Figlet(font='slant')

    #Makes the interface look better
    print(Fore.RED + f.renderText('Inventory'))
    print(Fore.YELLOW + f.renderText('Management'))
    print(Fore.GREEN + f.renderText('System'))

    #Instructions
    print(Fore.RED + "Use The following Commands :",end=" ")
    print(Fore.GREEN+ "Command in green",end=" ")
    print(Fore.YELLOW+ "Variables in yellow")


    #Adding item details
    print(Fore.WHITE + "Add Item     :",end=" ")
    print(Fore.GREEN + "add")

    #Removing an item
    print(Fore.WHITE + "Remove Item  :",end=" ")
    print(Fore.GREEN + "remove",end=" ")
    print(Fore.YELLOW + "<item_id>")

    #List items
    print(Fore.WHITE + "List Items   :",end=" ")
    print(Fore.GREEN + "list")

    #Export items
    print(Fore.WHITE + "Export list  :",end=" ")
    print(Fore.GREEN + "export",end=" ")
    print(Fore.YELLOW + "<filename>")

    #Checkout items
    print(Fore.WHITE + "Item Checkout:",end=" ")
    print(Fore.GREEN + "Checkout",end=" ")
    print(Fore.YELLOW + "<item_id>")

    #Checkin items
    print(Fore.WHITE + "Item Checkin :",end=" ")
    print(Fore.GREEN + "Checkin",end=" ")
    print(Fore.YELLOW + "<item_id>")

    #View item
    print(Fore.WHITE + "View Item    :",end=" ")
    print(Fore.GREEN + "view",end=" ")
    print(Fore.YELLOW + "<item_id>")

    #Search item
    print(Fore.WHITE + "Search Item  :",end=" ")
    print(Fore.GREEN + "search",end=" ")
    print(Fore.YELLOW + "<search_string>")

    #Compute total value
    print(Fore.WHITE + "Compute asset value:",end=" ")
    print(Fore.GREEN + "assetvalue")

    prompt = '(imis) '
    file = None

    @docopt_cmd
    def do_add(self,arg):
        """Usage: add"""
        additem()

    @docopt_cmd
    def do_list(self,arg):
        """Usage: list 
        """
        listitems()

    @docopt_cmd
    def do_remove(self, arg):
        """Usage: remove <item_id>

        """
        itemid=arg['<item_id>']
        remove(itemid)  

    @docopt_cmd
    def do_checkin(self, arg):
        """Usage: checkin <item_id>"""
        itemid=arg['<item_id>']
        check_in(itemid)

    @docopt_cmd
    def do_checkout(self, arg):
        """Usage: Checkout <item_id>
        """
        itemid=arg['<item_id>']
        check_out(itemid)

    @docopt_cmd
    def do_view(self, arg):
        """Usage: view <item_id> 
        
        """
        itemid=arg['<item_id>']
        view(itemid)

    @docopt_cmd
    def do_search(self, arg):
        """Usage: search <search_string> 
            
        """
        search_string=arg['<search_string>']
        search(search_string) 

    @docopt_cmd
    def do_export(self, args):
        """Usage: item_export <file_name>
            
        """               

        file_name = args['<file_name>']

        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        data = c.execute("SELECT * FROM Items")
        with open(file_name +'.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'item-name','description', 'amount_available', 'price', 'date_added', 'status'])
            writer.writerows(data)
        conn.commit()
        c.close()
        conn.close()

        f = Figlet(font='slant')
        print(Fore.GREEN + 'File exported, check your directory for the %s file'%(file_name))

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        f = Figlet(font='slant')
        print(Fore.GREEN + f.renderText('Goodbye'))

        exit()

    @docopt_cmd
    def do_assetvalue(self, arg):
        """Usage: assetvalue 
        """
        compute()



opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    ImisInteract().cmdloop()

print(opt)