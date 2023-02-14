"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: David Poslt
email: david.poslt@gmail.com
discord: David P#7919
"""
import getpass, sqlite3, task_template

pozdrav = 'Výtám vás v textovém analyzátoru, prvním projektu z Python Akademie'
format = "#" * (len(pozdrav) + 2)
print(f'{format} \n {pozdrav}\n{format}')


def checkUser(dbname):
    print('Pro pokračování se nejprve musíte přihlásit')
    username = input('username: ')
    password = getpass.getpass('password: ')

    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    statement = f"SELECT userName from users WHERE userName='{username}' AND userPass = '{password}';"
    cur.execute(statement)
    if not cur.fetchone():  # An empty result evaluates to False.
        print("Login failed")
    else:
        choiseText()

def main():
    choise = int(input('Choise text etc. 1 2 3: '))

    if choise != 1 and choise != 2 and choise != 3 and choise != 4:
        return 'Your choise is incorrect'
    else:
        choise_text = task_template.TEXTS[choise - 1]
        pocet_slov = choise_text.split()
        pocet_slov_velke_pismo = choise_text.capitalize()
        return f' pocet slov: {len(pocet_slov)} \n pocet slov zacinajici velkym pismem: {pocet_slov_velke_pismo}'



if __name__ == '__main__':
    # (checkUser('users.db'))
    # print(choiseText())
    print(main())
