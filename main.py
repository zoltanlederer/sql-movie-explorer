from load_data import get_connection
from query import query

connection = get_connection()
results = query(connection)
print('=>', results)