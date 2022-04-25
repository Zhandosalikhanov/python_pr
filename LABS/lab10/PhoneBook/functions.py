import psycopg2 as ps
from configparser import ConfigParser

# Function to configure database
def config(filename='credentials.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

# Function to connect to the server
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = ps.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

# Function to Create new table      
def CreatePhoneTable(name= 'PhoneBook'):
    # Commands as list
    command = f"""CREATE TABLE {name} (
            name TEXT PRIMARY KEY,
            phone TEXT
        )"""
    
    conn = None
    
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = ps.connect(**params)
        cur = conn.cursor()
        # create table
        cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        
        # Print success
        print(f"Successfully created table {name}")
        
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Function to Delete table             
def DeletePhoneTable(name= 'PhoneBook'):
    # Commands as list
    command = f"""DROP TABLE {name}"""
    
    conn = None
    
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = ps.connect(**params)
        cur = conn.cursor()
        # create table
        cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        
        # Print success
        print(f"Successfully deleted {name} table")
        
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Function to insert the data into the table
def InsertPhoneData(name, phone, table= 'phonebook'):
    
    comand = f"""INSERT INTO {table} (name, phone)
                VALUES ('{name}', '{phone}'); """
    
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = ps.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(comand)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
        
        # Print success
        print(f"Successfully inserted {name} user with {phone} phone number into the {table} table")
        
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Function to Change the username or the number
def ChangePhoneData(name, phone, change= 'phone', table= 'test'):
    
    # Commands
    change_phone = f"""UPDATE {table} 
                SET phone = %s WHERE name = %s"""
                
    change_name = f"""UPDATE {table} 
                SET name = %s WHERE phone = %s"""
                
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = ps.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the CHANGE statement
        if change == 'phone': cur.execute(change_phone, (phone, name))
        else: cur.execute(change_name, (name, phone))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
        
        # Print success
        if change == 'phone': print(f"Successfully changed {name} phone number to {phone}")
        
        else: print(f"Successfully changed {phone} user to {name}")
        
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
# Function to Delete row      
def DeletePhoneData(row, by= 'name', table= 'phonebook'):
    
    delete_data = f"""DELETE FROM {table}
                        WHERE {by} = '{row}'"""
                
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = ps.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the DELETE statement
        cur.execute(delete_data)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
        
        # Print success
        print(f"Successfully deleted {row} row")
        
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
# Function to show existing tables 
def show():
    
    comand = """SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'"""
    
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = ps.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(comand)
        # write the contents
        result = cur.fetchall()
        # close communication with the database
        cur.close()
        
        # Print Success
        if len(result):
            print(result)
            print("You are seeing existing tables")
        else:
            print("No tables exist")
        
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
# Function to show the contents of a table            
def view(table= 'phonebook', order= 'name'):
    
    comand = f""" SELECT * FROM {table} ORDER BY {order}"""
    
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = ps.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the SELECT statement
        cur.execute(comand)
        
        # print the contents
        for row in cur.fetchall():
            print(row[0], '\t', row[1])
            
        # close communication with the database
        cur.close()
        
        # Print Success
        print(f"You are seeing the '{table}' table ordered by {order}")
        
    except:
        print("No such table exist. You can create new table using 'cr' command or see existing tables with 'show' command")
    finally:
        if conn is not None:
            conn.close()
            