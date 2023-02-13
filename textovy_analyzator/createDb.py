import sqlite3, getpass
from sqlite3 import Error


def create_db(dbname):
    try:
        global connection
        connection = sqlite3.Connection(dbname, timeout=10)
        # global cursor
        cursor = connection.cursor()

        table = """
        CREATE TABLE IF NOT EXISTS users(
        person_id INTEGER PRIMARY KEY,
        userName text NOT NULL UNIQUE,
        userPass text NOT NULL
        )
        """

        cursor.execute(table)
        connection.commit()
        # connection.close()

    except Error as e:
        print(f'create db failed {e}')


def insert():
    # insert unsecured values
    cursor = connection.cursor()
    while True:
        userName = input('Enter new user => name (q for escape): ')
        if userName == 'q':
            return False

        userPass = getpass.getpass(f'Enter password for user =>  {userName}: ')

        try:
            cursor.execute('''
                            INSERT INTO users (userName, userPass)
            
                            VALUES
                            (?,?)
                        ''', (userName, userPass))
            connection.commit()

        except:
            return 'userName must be unique'



def select_for_test():
    cursor = connection.cursor()
    select = '''
        SELECT userName, userPass FROM users
    '''
    s = cursor.execute(select)
    rows = s.fetchall()
    for row in rows:
        print(rows)


if __name__ == '__main__':
    create_db('users.db')
    #print(insert())
    select_for_test()
