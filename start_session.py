#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    imis tcp <host> <port> [--timeout=<seconds>]
    imis serial <port> [--baud=<n>] [--timeout=<seconds>]
    imis (-i | --interactive)
    imis (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from colorama import init,Fore
init()
from pyfiglet import Figlet
from declaredb import Items,Logs,Base
from additems import additem
from listitems import listitems


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
    print(Fore.WHITE + "Add Item   :",end=" ")
    print(Fore.GREEN + "add_item",end=" ")
    print(Fore.YELLOW + "<item_name>",end=" ")
    print(Fore.YELLOW + "<description>",end=" ")
    print(Fore.YELLOW + "<available_num>",end=" ")
    print(Fore.YELLOW + "<price>")

    #Removing an item
    print(Fore.WHITE + "Remove Item:",end=" ")
    print(Fore.GREEN + "remove",end=" ")
    print(Fore.YELLOW + "<item_id>")

    #List items
    print(Fore.WHITE + "List Items :",end=" ")
    print(Fore.GREEN + "list")

    #Export items
    print(Fore.WHITE + "Export list:",end=" ")
    print(Fore.GREEN + "list --export",end=" ")
    print(Fore.YELLOW + "<filename>")

    #Checkout items
    print(Fore.WHITE + "Item Checkout:",end=" ")
    print(Fore.GREEN + "Checkout",end=" ")
    print(Fore.YELLOW + "<item_id>")

    #Checkin items
    print(Fore.WHITE + "Item Checkin:",end=" ")
    print(Fore.GREEN + "Checkin",end=" ")
    print(Fore.YELLOW + "<item_id>")

    #View item
    print(Fore.WHITE + "View Item:",end=" ")
    print(Fore.GREEN + "view",end=" ")
    print(Fore.YELLOW + "<item_id>")

    #Search item
    print(Fore.WHITE + "Search Item:",end=" ")
    print(Fore.GREEN + "search",end=" ")
    print(Fore.YELLOW + "<search_string>")

    #Compute total value
    print(Fore.WHITE + "Compute asset value:",end=" ")
    print(Fore.GREEN + "assetvalue")

    prompt = '(my_program) '
    file = None

    @docopt_cmd
    def do_add(self,arg):
        """Usage: add <item_name> <description> <available_num> <Price> [--timeout=<seconds>]"""
        
        item_name = arg['<item_name>']
        description=arg['<description>']
        available_num=arg['<available_num>']
        price=arg['<Price>']
        

        additem(item_name,description,int(available_num),int(price))

    @docopt_cmd
    def do_list(self, arg):
        """Usage: list 
        """

        listitems()

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    ImisInteract().cmdloop()

print(opt)