"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: David Poslt
email: david.poslt@gmail.com
discord: David P#7919
"""
import getpass, sqlite3

pozdrav = 'Výtám vás v textovém analyzátoru, prvním projektu z Python Akademie'
format = "#"*(len(pozdrav)+2)
print(f'{format} \n {pozdrav}\n{format}')

def checkUser(dbname):
    print('Pro pokračování se nejprve musíte přihlásit')
    #jmeno = input('Zadejte registrační jméno: ')
    #password = getpass.getpass('Zadejte heslo: ')
    
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    
    select = '''
        SELECT userName, userPass FROM users
    '''
    s = cur.execute(select)
    for i in s:
        print(i)
