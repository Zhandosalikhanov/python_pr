import psycopg2 as ps, re, csv
from configparser import ConfigParser

# All the required commands
commands = {
    'select':       """SELECT name FROM {}
                    WHERE name = '{}' AND surname = '{}'""",
    
    'create':      """CREATE TABLE {} (
                    name TEXT,
                    surname TEXT,
                    phone TEXT)""",
            
    'insert':       """INSERT INTO {} (name, surname, phone)
                    VALUES ('{}', '{}', '{}') """,
    
    'update':       """UPDATE {} 
                    SET phone = {} WHERE name = '{}' AND surname = '{}'""",
    
    'delete':       """DELETE FROM {} 
                    WHERE name = '{}' OR surname = '{}' OR phone = '{}'""",
                
    'select_pag':   """SELECT * FROM {}
                    ORDER BY {} LIMIT {} OFFSET {}""",
    
    'search':       """SELECT * FROM {} 
                    WHERE name ILIKE '{}' OR surname ILIKE '{}' OR phone ILIKE '{}'"""
    
}

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

# To check if the number is valid in Kazakhstan
def isValid_KZ(number):
    match = re.search("[a-zA-Z]", number)
    
    if (
        ((number[0] == '+' and len(number) == 12)
        or 
        (number[0] == '8' and len(number) == 11))
        and
        not match):
        return True
    
    return False

# Class with executable functions
class CMD:
    def __init__(self, cursor):
        self.cur = cursor
    
    def doEXIST(self, name, surname):
        # Function to check if the user is already exists
        self.cur.execute(commands['select'].format(self.table, name, surname))
        return len(self.cur.fetchall())
    
    def create(self):    
        # To create a new table
        self.cur.execute(commands['create'].format(self.name))
        print("TABLE created")
    
    def insert(self):        
        # To insert list of data and update if already exists
        invalid = []
        updated = 0
        
        for data in self.list:   
            # Check if data exist and is the number is valid
            if not self.doEXIST(data[0], data[1]):
                if isValid_KZ(data[2]):
                    self.cur.execute(commands['insert'].format(self.table, data[0], data[1], data[2]))
                else:
                    invalid.append(data)
                
            else:
                if isValid_KZ(data[2]):
                    updated += 1
                    self.cur.execute(commands['update'].format(self.table, data[2], data[0], data[1]))
                else:
                    invalid.append(data)
        
        # Print the executed command and all invalid data (if any)            
        if (len(invalid) != len(self.list) and updated != len(self.list) - len(invalid)):
                                        print("DATA inserted")
        if updated:                     print("DATA updated")
        if len(invalid):                print("INVALID data:\n", invalid)
    
    def delete(self):    
        # To delete data by name or surname
        given = None
        if   self.name    != None: given = self.name
        elif self.surname != None: given = self.surname
        elif self.phone   != None: given = self.phone
        
        if given:
            self.cur.execute(commands['delete'].format(self.table, given, given, given))
            print("DATA deleted")
        else:
            print("No data to delete from")
    
    def select(self):   
       # To query data with pagination 
        self.cur.execute(commands['select_pag'].format(self.table, self.order, self.limit, self.offset))
        data = self.cur.fetchall()
        print("The queried data:\n", data)
    
    def search(self):    
        # To search data with given pattern
        if self.pattern:
            self.cur.execute(commands['search'].format(self.table, self.pattern, self.pattern, self.pattern))
            data = self.cur.fetchall()
            print("The data satistifying the pattern:\n", data) if len(data) else print("No matching data")
        else:
            print("No pattern to search by")
 
    def update(self):       
        # To change phone number by given name    
        self.cur.execute(commands['update'].format(self.table, self.phone, self.name, self.surname))
        print("DATA updated")
  
    def upload(self):      
        # To upload data from csv file
        if self.path:
            with open(self.path) as csv_file:
                reader = csv.reader(csv_file)
                next(reader)
                for row in reader:
                    self.name = row[0]
                    self.surname = row[1]
                    self.phone = row[2]
                    self.insert()
        else:
            print("No PATH given")

def execute(command, **kargs):
    """The function to execute the given commands in PostgreSQL database

    Args:
        command (str) : String-name of the command
        **kargs (dict): A dictionary with needed arguments
                        EXAMPLE: execute('insert', name= User, surname= Admin, phone= 83450632143)
                        If some data is not given, default is picked or error is printed
    """
    
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = ps.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        
        # Create the class
        C = CMD(cur)
        
        # Given keyword arguments
        C.table   = kargs.get('table', 'test')
        C.name    = kargs.get('name', None)
        C.surname = kargs.get('surname', None)
        C.phone   = kargs.get('phone', None)
        C.order   = kargs.get('order', 'name')
        C.limit   = kargs.get('limit', 999)
        C.offset  = kargs.get('offset', 0)
        C.list    = kargs.get('list', [(C.name, C.surname, C.phone)])
        C.pattern = kargs.get('pattern', None)
        C.path    = kargs.get('path', None)
        
        call = {
            'create'    : C.create,
            'insert'    : C.insert,
            'delete'    : C.delete,
            'select_pag': C.select,
            'search'    : C.search,
            'update'    : C.update,
            'upload'    : C.upload
        }
        
        call[command]()
        
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
        
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
if __name__ == '__main__':
    print("TEST OUTPUT:\n")
    # execute('insert',  list = [("Jenifer", "Lulably", "89996663322"), ("Inerajen", "Dirakgua", "+71236548899")])
    # execute('select_pag', limit= 3, offset= 1, order= 'phone')
    # execute('search', pattern= "%jen%")