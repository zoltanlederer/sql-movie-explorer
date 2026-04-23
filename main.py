"""
CLI tool to query a personal media library using SQLite.
"""

import argparse
from load_data import get_connection
from query import query

parser = argparse.ArgumentParser(description='CLI tool to query a personal media library')
parser.add_argument('-g', '--genres', help='Filter by genre, e.g. "Action", "Comedy"')
parser.add_argument('-y', '--year', help='Filter by year, e.g. "1990"')
parser.add_argument('-r', '--rating', help='Filter by minimum rating, e.g. "6.5"')
parser.add_argument('-m', '--media-type', help='Filter by media type. Options: "movie" or "tv_show"')
parser.add_argument('-t', '--title', help='Filter by title, e.g. "Batman"')
parser.add_argument('-o', '--output', default='export.csv', help='path and filename to save the export CSV e.g. "export.csv" or "/Users/zoli/data/export.csv"')
args = parser.parse_args()

output = args.output

connection = get_connection()
# results = query(connection, genres='action', year='1985')
results = query(connection, title='batman', media_type='movie')
print(results)


# python main.py --genre Action --year 2010 --type movie