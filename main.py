"""
CLI tool to query a personal media library using SQLite.
"""

import argparse
from load_data import get_connection
from query import query

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CLI tool to query a personal media library')
    parser.add_argument('-g', '--genres', help='Filter by genre, e.g. "Action", "Comedy"')
    parser.add_argument('-y', '--year', help='Filter by year, e.g. "1990"')
    parser.add_argument('-r', '--rating', help='Filter by minimum rating, e.g. "6.5"')
    parser.add_argument('-m', '--media-type', help='Filter by media type. Options: "movie" or "tv_show"')
    parser.add_argument('-t', '--title', help='Filter by title, e.g. "Batman"')
    parser.add_argument('-o', '--output', nargs='?', const='export.csv', help='Save results to CSV. Optionally provide a filename, e.g. "results.csv". Defaults to "export.csv" if no filename is given.')
    args = parser.parse_args()

    connection = get_connection()
    results = query(connection, genres=args.genres, year=args.year, imdb_rating=args.rating, media_type=args.media_type, title=args.title)
    print(results)
    if args.output: # save result to CSV
        full_results = query(connection, genres=args.genres, year=args.year, imdb_rating=args.rating, media_type=args.media_type, title=args.title, full=True)
        full_results.drop(columns=['index'], inplace=True)
        full_results.to_csv(args.output, index=False)
        print(f'Results saved to {args.output}')
