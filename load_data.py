"""
Loading and setting up the database
"""

from pathlib import Path
import argparse
import sys
import sqlite3
import pandas as pd

parser = argparse.ArgumentParser(description='loading and setting up the database.')
parser.add_argument('--import-path', default='./data/master.csv', help='add the path of the import file, or use the default "/data/master.csv"')
args = parser.parse_args()

def load_csv(filepath):
    """ Load csv file including error handling """
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
         print(f"File not found: {filepath}")
         sys.exit()
    except IsADirectoryError:
        print(f"Is a directory: {filepath}")
        sys.exit()


def get_connection():
    """ Create a connection to the database """
    return sqlite3.connect('data/media.db')

 
def import_data(df, connection):
    """ Write DataFrame into database """
    return df.to_sql(name='media', con=connection, if_exists='replace')


def db_exists():
    """ Check database exists """
    database_check = Path('./data/media.db').exists()
    if database_check:
        answer = input(f'The database already exists. Would you like to replace it or quit?`\n To replace press "Enter", to quit press "q": ')
        if answer == 'q':
            sys.exit()
    return False            

filepath = Path(args.import_path)
df = load_csv(filepath)
connection = get_connection()
db_exist = db_exists()

if db_exists:
    rows = import_data(df, connection)
    print(f"Database created with {rows} rows.")
