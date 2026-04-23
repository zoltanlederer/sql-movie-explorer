"""
SQL query functions for the media database.
"""

import pandas as pd

def query(connection, genres=None, year=None, imdb_rating=None, media_type=None, title=None):
    """
    Query the media database with optional filters.
    Returns a DataFrame with all matching rows.
    If no filters are provided, returns the full database.
    """
    conditions = []
    values = []
    
    if genres:
        conditions.append('genres LIKE ?')
        values.append(f'%{genres}%')

    if year:
        conditions.append('year = ?')
        values.append(year)

    if imdb_rating:
        conditions.append('imdb_rating >= ?')
        values.append(imdb_rating)

    if media_type:
        conditions.append('type = ?')
        values.append(media_type)
        
    if title:
        conditions.append('title LIKE ?')
        values.append(f'%{title}%')

    base = 'SELECT imdb_id, title, year, genres, runtime_mins, type, number_of_seasons, number_of_episodes, imdb_rating, directors FROM media'
    if conditions:
        base += ' WHERE ' + ' AND '.join(conditions)

    return pd.read_sql(base, connection, params=tuple(values))
