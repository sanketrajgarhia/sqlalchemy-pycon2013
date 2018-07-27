import os
from termcolor import colored, cprint

from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String

#Restore the state of metadata.db - prior to run
os.system('git checkout -- metadata.db')

#Function to print heading and code
def print_output(number,code,heading):
    os.system('clear')
    number_print = "\nNo {}.".format(number)
    print(number_print)
    print("_"*len(number_print))
    print("{}".format(code).rstrip('\n'))
    print("\n{}".format(heading))
    print("-"*len(heading.split('\n')[0]))
    return

################################################################################

#1
#Using the MetaData() object to containg the structure of the schema.
#Create the 'user' table.
number = 1
code = """
metadata = MetaData()
user_table = Table('user', metadata,
    Column('id', Integer, primary_key = True),
    Column('name', String),
    Column('fullname', String))
"""
heading = "Listing the attributes of user_table."
print_output(number,code,heading)

metadata = MetaData()
user_table = Table('user', metadata,
    Column('id', Integer, primary_key = True),
    Column('name', String),
    Column('fullname', String))

#List attributes of user_table
print("user_table.name : {}". format(user_table.name))
print("user_table.columns : {}".format(user_table.columns))
print("user_table.columns.id : {}".format(user_table.columns.id))
print("user_table.columns.id.type : {}".format(user_table.columns.id.type))
print("user_table.columns.name.name : {}".format(user_table.columns.name.name))
print("user_table.columns.keys() : {}".format(user_table.columns.keys()))
name_column = user_table.columns.name
print("name_column : {}".format(name_column))
print("name_column.table : {}".format(name_column.table))
print("user_table.primary_key : {}".format(user_table.primary_key))
print("user_table.select() : {}".format(user_table.select()))

input("\nEnter to continue...")
################################################################################

os.system('clear')
print("\n"* 5)
cprint("END".rjust(38, " "), 'blue', attrs=['bold'])
heading = "NOTE: RESET YOUR GIT : git checkout -- metadata.db"
heading = heading.rjust(( len(heading) + ((80 - len(heading)) // 2)), " ")
cprint('{}'.format(heading), 'red', attrs=['blink','bold'])
print("\n"* 5)