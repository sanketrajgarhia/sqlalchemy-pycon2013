import os
from termcolor import colored, cprint

from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import ForeignKey, ForeignKeyConstraint
from sqlalchemy import Integer, String, DateTime, Numeric, Enum
from sqlalchemy import Unicode, UnicodeText
from sqlalchemy import create_engine, inspect

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

#2
#Using the metadata.create_all(engine) method to create all tables in a schema.
#If a table exists then it will not be created again.
#Add the 'user' table to the schema.
number += 1
code = """
engine = create_engine("sqlite:///metadata.db")
metadata.create_all(engine)
"""
heading = "Using the metadata.create_all(engine) method to create all tables\n\
in a schema.\nIf a table exists then it will not be created again.\n\
Add the 'user' table to the schema."
print_output(number,code,heading)

engine = create_engine("sqlite:///metadata.db")
metadata.create_all(engine)

input("\nEnter to continue...")

################################################################################

#3
#Creating a table with different data types.
#Using the table object's create(engine) method to create the table
#in the database.
number += 1
code = """
table_fancy = Table('fancy',metadata,
                     Column(key, String(50), primary_key = True),
                     Column(timestamp, DateTime),
                     Column(amount, Integer(10,2)),
                     Column(type, Enum('a', 'b', 'c'))
                    )
table_fancy.create(engine)
"""
heading = "Creating a table with different data types and using the table \n\
object's create(engine) method to create the table\n\
in the database."
print_output(number,code,heading)

table_fancy = Table('fancy',metadata,
                     Column('key', String(50), primary_key = True),
                     Column('timestamp', DateTime),
                     Column('amount', Numeric(10,2)),
                     Column('type', Enum('a', 'b', 'c'))
                    )
table_fancy.create(engine)

input("\nEnter to continue...")

################################################################################

#4
#Creating a table with Foreign Key.
#Using the table object's create(engine) method to create the table
#in the database.
number += 1
code = """
address_table = Table('address',metadata,
                      Column('id', Integer, primary_key = True),
                      Column('email_address',String(100), nullable = False),
                      Column('user_id', Integer, ForeignKey('user.id'))
                      )
address_table.create(engine)
"""
heading = "Creating a table with Foreign Key constraint.\n\
Using the table object's create(engine) method to \n\
create the table in the database."
print_output(number,code,heading)

address_table = Table('address',metadata,
                      Column('id', Integer, primary_key = True),
                      Column('email_address',String(100), nullable = False),
                      Column('user_id', Integer, ForeignKey('user.id'))
                      )
address_table.create(engine)

input("\nEnter to continue...")

################################################################################

#5
#Creating a table with Composite Foreign Key.
number += 1
code = """
story_table = Table('story', metadata,
                    Column('story_id', Integer, primary_key = True),
                    Column('version_id', Integer, primary_key = True),
                    Column('headline', Unicode(100), nullable = False),
                    Column('body', UnicodeText)
                    )

published_table = Table('published', metadata,
                        Column('pub_id', Integer, primary_key = True),
                        Column('pub_timestamp', DataTime, nullable = false),
                        Column('story_id', Integer),
                        Column('version_id', Integer),
                        ForeignKeyConstraint(
                        ['story_id', 'version_id'],
                        ['story.story_id','story.version_id'])
                        )
metadata.create_all(engine)
"""
heading = "Creating a table with Composite Foreign Key constraint."
print_output(number,code,heading)

story_table = Table('story', metadata,
                    Column('story_id', Integer, primary_key = True),
                    Column('version_id', Integer, primary_key = True),
                    Column('headline', Unicode(100), nullable = False),
                    Column('body', UnicodeText)
                    )

published_table = Table('published', metadata,
                        Column('pub_id', Integer, primary_key = True),
                        Column('pub_timestamp', DateTime, nullable = False),
                        Column('story_id', Integer),
                        Column('version_id', Integer),
                        ForeignKeyConstraint(
                        ['story_id', 'version_id'],
                        ['story.story_id','story.version_id'])
                        )
metadata.create_all(engine)

input("\nEnter to continue...")

################################################################################

#6
#Exercise - create the 'network' Table.
number += 1
code = """
network_table = Table('network', metadata,
                      Column('network_id', Integer, primary_key = True),
                      Column('name', String(100), nullable = False),
                      Column('created_at', DateTime, nullable = False),
                      Column('owner_id',Integer, ForeignKey('user.id'))
                     )
metadata.create_all(engine)
"""
heading = "Exercise - create the 'network' Table."
print_output(number,code,heading)

network_table = Table('network', metadata,
                      Column('network_id', Integer, primary_key = True),
                      Column('name', String(100), nullable = False),
                      Column('created_at', DateTime, nullable = False),
                      Column('owner_id',Integer, ForeignKey('user.id'))
                     )
metadata.create_all(engine)

input("\nEnter to continue...")

################################################################################

#7
#Reflection - Getting the 'user' Table from the database into python.
number += 1
code = """
metadata2 = MetaData()
user_reflected_table = Table('user',metadata2,
                             autoload = True, autoload_with = engine)
print(user_reflected_table)
"""
heading = "Reflection - Getting the 'user' Table from the database into python."
print_output(number,code,heading)

metadata2 = MetaData()
user_reflected_table = Table('user',metadata2,
                             autoload = True, autoload_with = engine)
print(user_reflected_table.columns)

input("\nEnter to continue...")

################################################################################

#8
#Reflection - Using inspect(engine) method.

number += 1
code = """
inspector = inspect(engine)
print("inspector.get_table_names() : {}".format(nspector.get_table_names()))
print("inspector.get_columns('address') : {}"
      .format(inspector.get_columns('address')))
print("inspector.get_foreign_keys('published') : {}"
      .format(inspector.get_foreign_keys('published')))
"""
heading = "Reflection - Using inspect(engine) method."
print_output(number,code,heading)

inspector = inspect(engine)
print("inspector.get_table_names() : {}".format(inspector.get_table_names()))
print("inspector.get_columns('address') : {}"
      .format(inspector.get_columns('address')))
print("inspector.get_foreign_keys('published') : {}"
      .format(inspector.get_foreign_keys('published')))

input("\nEnter to continue...")

################################################################################

#9
#Exerice - Reflect 'network' table and display column names onlyself.
#Using "inspector", print a list of all table names that include a column
#called 'story_id'.

number += 1
code = """
reflected_network_table = Table('network', metadata2,
                                autoload = True, autoload_with = engine)
for column in reflected_network_table.columns.keys():
    print(column)

output_title = "\nListing all tables that have the column - 'story_id'"
print(output_title)
print("-" * len(output_title))

for tb in inspector.get_table_names():
    for cl in inspector.get_columns(tb):
        if cl['name'] == 'story_id':
            print(tb)
            break
"""
heading = "Exerice - Reflect 'network' table and display column names onlyself."
heading += "\nUsing inspector, print a list of all table names that include"
heading += "\na column called 'story_id'."
print_output(number,code,heading)

reflected_network_table = Table('network', metadata2,
                                autoload = True, autoload_with = engine)
for column in reflected_network_table.columns.keys():
    print(column)

output_title = "\nListing all tables that have the column - 'story_id'"
print(output_title)
print("-" * len(output_title))

for tb in inspector.get_table_names():
    for cl in inspector.get_columns(tb):
        if cl['name'] == 'story_id':
            print(tb)
            break

input("\nEnter to continue...")

################################################################################

os.system('clear')
print("\n"* 5)
cprint("END".rjust(38, " "), 'blue', attrs=['bold'])
heading = "NOTE: RESET YOUR GIT : git checkout -- metadata.db"
heading = heading.rjust(( len(heading) + ((80 - len(heading)) // 2)), " ")
cprint('{}'.format(heading), 'red', attrs=['blink','bold'])
print("\n"* 5)
