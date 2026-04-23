# SQL Movie Explorer

CLI tool to query a personal media library using SQLite and Python.

Takes the master CSV exported by the Media CSV Loader script and loads it into a SQLite database.
Provides a CLI interface to filter by genre, year, rating, or type (movie vs TV show).
Results print cleanly in the terminal with an option to export to CSV.

## Requirements

- Python 3.x
- pandas

## Installation

Clone the repo:
```bash
git clone https://github.com/zoltanlederer/sql-movie-explorer.git
cd sql-movie-explorer
```

Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Place your master CSV file in the `data/` folder as `data/master.csv`.

## Usage & Options

Usage:
```bash
python3 main.py
```

Options:
```bash
  -h, --help        Show this help message and exit
  -g, --genres      Filter by genre, e.g. "Action", "Comedy"
  -y, --year        Filter by year, e.g. "1990"
  -r, --rating      Filter by minimum rating, e.g. "6.5"
  -m, --media-type  Filter by media type. Options: "movie" or "tv_show"
  -t, --title       Filter by title, e.g. "Batman"
  -o, --output      Save results to CSV. Optionally provide a filename, e.g. "results.csv". Defaults to "export.csv" if no filename is given.
```

## Examples
```bash
python3 main.py --genres "action" --year "1985"
------------------------------
Found 10 results.
------------------------------
                          title  year             genres  runtime_mins   type  number_of_seasons  number_of_episodes  imdb_rating           directors    imdb_id
0                      Commando  1985  Action, Adventure            91  movie               <NA>                <NA>          6.7      Mark L. Lester  tt0088944
1                My Lucky Stars  1985     Action, Comedy            96  movie               <NA>                <NA>          6.3   Sammo Kam-Bo Hung  tt0089177
2                  Police Story  1985     Action, Comedy           100  movie               <NA>                <NA>          7.5         Jackie Chan  tt0089374
3     The Man with One Red Shoe  1985     Action, Comedy            92  movie               <NA>                <NA>          5.7        Stan Dragoti  tt0089543
4               Miami Supercops  1985     Action, Comedy            96  movie               <NA>                <NA>          6.1      Bruno Corbucci  tt0089591
5                 The Protector  1985  Action, Adventure            95  movie               <NA>                <NA>          5.7   James Glickenhaus  tt0089847
6    Rambo: First Blood Part II  1985  Action, Adventure            95  movie               <NA>                <NA>          6.5  George P. Cosmatos  tt0089880
7                     Red Sonja  1985  Action, Adventure            94  movie               <NA>                <NA>          5.1   Richard Fleischer  tt0089893
8              A View to a Kill  1985  Action, Adventure           131  movie               <NA>                <NA>          6.3           John Glen  tt0090264
9  Twinkle, Twinkle Lucky Stars  1985     Action, Comedy            94  movie               <NA>                <NA>          6.2   Sammo Kam-Bo Hung  tt0090342


# Save the results to a CSV file
python3 main.py --genres "crime" --media-type "tv_show" --output "results.csv"    
------------------------------
Found 84 results.
------------------------------
               title  year         genres  runtime_mins     type  number_of_seasons  number_of_episodes  imdb_rating directors    imdb_id
0       Magnum, P.I.  1980   Drama, Crime            45  tv_show                  8                 162          7.5      None  tt0080240
1       Knight Rider  1982   Drama, Crime            48  tv_show                  4                  90          6.9      None  tt0083437
2         The A-Team  1983  Crime, Comedy            45  tv_show                  5                  95          7.5      None  tt0084967
3           MacGyver  1985   Crime, Drama            45  tv_show                  7                 139          7.6      None  tt0088559
4           Baywatch  1989   Drama, Crime            42  tv_show                  9                 198          5.5      None  tt0096542
..               ...   ...            ...           ...      ...                ...                 ...          ...       ...        ...
79        The Rookie  2018   Crime, Drama            43  tv_show                  7                 126          8.0      None  tt7587890
80      Breaking Bad  2008   Drama, Crime            48  tv_show                  5                  62          9.5      None  tt0903747
81           Reacher  2022   Crime, Drama            50  tv_show                  3                  24          8.0      None  tt9288030
82              Next  2020   Drama, Crime            45  tv_show                  1                  10          6.7      None  tt9315054
83  FBI: Most Wanted  2020   Drama, Crime            45  tv_show                  6                 108          6.9      None  tt9742936

[84 rows x 10 columns]
------------------------------
Results saved to results.csv
------------------------------
```

## Reloading the Database

To manually reload the database after updating your CSV:
```bash
python3 load_data.py
```