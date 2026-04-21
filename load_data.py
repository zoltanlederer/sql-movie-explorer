"""
Loading and setting up the database
"""

from pathlib import Path
import argparse
import sys
import sqlite3
import pandas as pd

parser = argparse.ArgumentParser(description='Loading and setting up the database.')
parser.add_argument('--import-path', default='./data/master.csv', help='Path to the CSV file to import.')
args = parser.parse_args()

def load_csv(filepath):
    """Load CSV file with error handling."""
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit()
    except IsADirectoryError:
        print(f"Expected a file, got a directory: {filepath}")
        sys.exit()


def get_connection():
    """Create and return a connection to the SQLite database."""
    return sqlite3.connect('data/media.db')


def import_data(df, connection):
    """Write DataFrame into the database."""
    return df.to_sql(name='media', con=connection, if_exists='replace')


def db_exists():
    """If the database already exists, ask the user to confirm overwrite."""
    if Path('./data/media.db').exists():
        answer = input('The database already exists. Press Enter to replace it, or "q" to quit: ')
        if answer == 'q':
            sys.exit()


# this only runs if the file is run directly
if __name__ == '__main__':
    filepath = Path(args.import_path)
    df = load_csv(filepath)       # fail early if CSV not found
    db_exists()                   # ask the user if needed, exit if they say q
    connection = get_connection()
    rows = import_data(df, connection)
    print(f"Database created with {rows} rows.")