# Import all functions for sql management and also csv library to read csv file
from functions import *
import csv

# Function to show the instructions 
def show_inst():
    ins = open('instructions.txt', 'r')
    print(ins.read())
    ins.close()

# Some varibales
command = ''
table_name = None

# Show instructions
show_inst()

# While user hasn't quit
while command != 'q':
    # Read command
    command = input("\nEnter a command: ")
    
    # Show instructions again, show existing tables or quit
    if command == 'help': show_inst()
    elif command == 'show': show()
    elif command == 'q': break

    # Create new table
    elif command == 'cr':
        table_name = input("\tEnter table name: ")
        CreatePhoneTable(table_name)
    
    # Delete specified table        
    elif command == 'del':
        name = input("\tEnter table name: ")
        DeletePhoneTable(name)
        
    # View specified table        
    elif command == 'v':
        table_name = input("\tEnter table name: ")
        order = input("\tEnter ordering law (name or phone): ")
        view(table_name, order)

    # Insert data to the table
    elif command == 'ins':
        name = input("\tEnter username: ")
        phone = input("\tEnter phone number: ")
        
        if table_name is None:
            table_name = input("\tEnter table name: ")
            
        InsertPhoneData(name, phone, table_name)

    # Upload data from csv file
    elif command == 'up':
        name = input("Enter a csv file name: ")
        
        try:
            f = open(f'{name}.csv')
            csv_read = csv.reader(f)
            next(csv_read)
            
            for row in csv_read:
                InsertPhoneData(row[0], row[1], table_name)
            
            print(f"successfully uploaded data from {name}.csv file")
        except:
            print("No such file exist")
        finally:
            f.close()

    # Change data
    elif command == 'ch':
        type = input("\tBy what value you want to modify (name or phone): ")
        
        if table_name is None:
            table_name = input("\tEnter table name: ")
            
        if type == 'name':
            name = input("\tEnter user name: ")
            phone = input("\tEnter new number: ")
            ChangePhoneData(name, phone, 'phone', table_name)
            
        elif type == 'phone':
            phone = input("\tEnter user number: ")
            name = input("\tEnter new name: ")
            ChangePhoneData(name, phone, 'name', table_name)
    
    # Delete row           
    elif command == 'del_row':
        type = input("By what value you want to delete (name or phone): ")
        if type == 'name':
            name = input("\tEnter user name: ")
            DeletePhoneData(name, type, table_name)
        elif type == 'phone':
            phone = input("\tEnter user number: ")
            DeletePhoneData(phone, type, table_name)

    # Wrong syntax
    else:
        print("Invalid input")