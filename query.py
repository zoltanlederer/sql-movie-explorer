"""
It handles all the SQL queries
"""

import pandas as pd

def query(connection, genre=None, year=None, rating=None, media_type=None, title=None):
    return pd.read_sql('SELECT * FROM media', connection)
    # return pd.read_sql(query, connection)