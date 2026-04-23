"""
CLI tool to query a personal media library using SQLite.
"""

import argparse
from pathlib import Path
from load_data import load_csv, get_connection, import_data, db_exists
from query import query

if __name__ == '__main__':
    # Set up CLI arguments
    parser = argparse.ArgumentParser(description='CLI tool to query a personal media library')
    parser.add_argument('-g', '--genres', help='Filter by genre, e.g. "Action", "Comedy"')
    parser.add_argument('-y', '--year', help='Filter by year, e.g. "1990"')
    parser.add_argument('-r', '--rating', help='Filter by minimum rating, e.g. "6.5"')
    parser.add_argument('-m', '--media-type', help='Filter by media type. Options: "movie" or "tv_show"')
    parser.add_argument('-t', '--title', help='Filter by title, e.g. "Batman"')
    parser.add_argument('-o', '--output', nargs='?', const='export.csv', help='Save results to CSV. Optionally provide a filename, e.g. "results.csv". Defaults to "export.csv" if no filename is given.')
    args = parser.parse_args()

    # Set up database
    if not Path('./data/media.db').exists():
        df = load_csv(Path('./data/master.csv'))
        db_exists()
        connection = get_connection()
        import_data(df, connection)
        print('Database created.')
    else:
        connection = get_connection()

    # Run query and display results
    results = query(connection, genres=args.genres, year=args.year, imdb_rating=args.rating, media_type=args.media_type, title=args.title)
    
    if results.shape[0] > 0:
        print('-' * 30)
        result_word = 'result' if results.shape[0] == 1 else 'results'
        print(f'Found {results.shape[0]} {result_word}.')
        print('-' * 30)

        # Convert float columns to nullable integers for clean terminal display
        for col in ['year', 'runtime_mins', 'number_of_seasons', 'number_of_episodes']:
            results[col] = results[col].astype('Int64')

        print(results)
    else:
        print('No results found. Try different filters.')

    # Export results to CSV
    if args.output:
        if results.shape[0] > 0:
            full_results = query(connection, genres=args.genres, year=args.year, imdb_rating=args.rating, media_type=args.media_type, title=args.title, full=True)
            full_results.drop(columns=['index'], inplace=True)
            full_results.to_csv(args.output, index=False)
            print('-' * 30)
            print(f'Results saved to {args.output}')
            print('-' * 30)