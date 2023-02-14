import sqlite3, getpass
from sqlite3 import Error

def create_db(dbname):
    try:
        global connection
        connection = sqlite3.Connection(dbname, timeout=10)
        #global cursor
        cursor = connection.cursor()
        
        table = """
        CREATE TABLE IF NOT EXISTS users(
        person_id INTEGER PRIMARY KEY,
        userName text NOT NULL UNIQUE,
        userPass text NOT NULL UNIQUE
        )
        """
        
        cursor.execute(table)
        connection.commit()
        #connection.close()
            
    except Error as e:
        print(f'create db failed {e}')
        
def insert():
    # insert unsecured values
    cursor = connection.cursor()
    userName = input('Založ nového uživatele => jméno: ')
    userPass = getpass.getpass(f'Vlož heslo pro uživatele {userName}: ')
    cursor.execute('''
          INSERT INTO users (userName, userPass)

                VALUES
                (?,?)
          ''', (userName, userPass))

    connection.commit()
    
def select_for_test():
    
    cursor = connection.cursor()
    select = '''
        SELECT userName, userPass FROM users
    '''
    s = cursor.execute(select)
    for i in s:
        print(i)
        